from fastapi import APIRouter, HTTPException
from typing import Callable

from app.services.trapezoidal import trapezoidal_rule
from app.services.boole import boole_rule
from app.services.simpson_abierto import simpson_abierto
from app.utils.parser import parse_function
from app.services.simpson_1_3 import simpson_1_3
from app.services.simpson_3_8 import simpson_3_8

from app.models.integration_models import IntegrationRequest, IntegrationResponse

router = APIRouter(
    prefix="/integration",
    tags=["integration"],
)


def _parse(data: IntegrationRequest) -> Callable:
    """Parsea la expresión matemática del request. Lanza HTTPException 400 si es inválida."""
    try:
        return parse_function(data.f)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def _run(service_fn, *args):
    """
    Ejecuta un servicio de integración capturando errores numéricos en tiempo de evaluación.

    Raises:
        HTTPException 400: OverflowError, ZeroDivisionError o ValueError del servicio.
        HTTPException 500: Cualquier error inesperado.
    """
    try:
        return service_fn(*args)
    except OverflowError:
        raise HTTPException(
            status_code=400,
            detail="La función produce valores demasiado grandes para el intervalo dado. "
            "Intenta reducir el intervalo [a, b].",
        )
    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="La función no está definida en algún punto del intervalo dado. "
            "Verifica que f(x) sea continua en [a, b].",
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error inesperado al evaluar la función: {e}"
        )


@router.post("/trapezoidal")
def trapezoidal_endpoint(data: IntegrationRequest) -> IntegrationResponse:
    """
    Endpoint para calcular la integral definida de una función usando la regla trapezoidal.

    Recibe una función como string, los límites de integración y el número de subintervalos.
    Devuelve la aproximación numérica de la integral.

    Args:
        data: Objeto JSON con los siguientes campos:
            - function: Expresión matemática en términos de x. Ej: 'x**2', 'sin(x)'.
            - a: Límite inferior del intervalo de integración.
            - b: Límite superior del intervalo de integración.
            - n: Número de subintervalos (trapecios). Mayor valor = mayor precisión.

    Returns:
        Objeto JSON con los siguientes campos:
            - method: Método numérico utilizado (ej: "trapezoidal").
            - function: Expresión integrada.
            - a: Límite inferior usado.
            - b: Límite superior usado.
            - n: Número de subintervalos usado.
            - result: Resultado aproximado de la integral.
    """
    f = _parse(data)
    result = _run(trapezoidal_rule, f, data.a, data.b, data.n)
    return IntegrationResponse(
        method="trapezoidal", f=data.f, a=data.a, b=data.b, n=data.n, result=result
    )


@router.post("/boole")
def boole_endpoint(data: IntegrationRequest) -> IntegrationResponse:
    """
    Endpoint para calcular la integral definida de una función usando la regla de Boole (Newton-Cotes 5 puntos).

    Requiere que n sea múltiplo de 4.

    Recibe una función como string, los límites de integración y el número de subintervalos.
    Devuelve la aproximación numérica de la integral.

    Args:
        data: Objeto JSON con los siguientes campos:
            - function: Expresión matemática en términos de x. Ej: 'x**2', 'sin(x)'.
            - a: Límite inferior del intervalo de integración.
            - b: Límite superior del intervalo de integración.
            - n: Número de subintervalos. Debe ser múltiplo de 4. Mayor valor = mayor precisión.
    Returns:
        Objeto JSON con los siguientes campos:
            - method: Método numérico utilizado (ej: "boole").
            - function: Expresión integrada.
            - a: Límite inferior usado.
            - b: Límite superior usado.
            - n: Número de subintervalos usado.
            - result: Resultado aproximado de la integral.
    """
    f = _parse(data)
    result = _run(boole_rule, f, data.a, data.b, data.n)
    return IntegrationResponse(
        method="boole", f=data.f, a=data.a, b=data.b, n=data.n, result=result
    )


@router.post("/simpson-abierto")
def simpson_abierto_endpoint(data: IntegrationRequest) -> IntegrationResponse:
    """
    Endpoint para calcular la integral definida de una función usando la regla de Simpson abierto compuesta.

    Requiere que n sea par.

    Recibe una función como string, los límites de integración y el número de subintervalos.
    Devuelve la aproximación numérica de la integral.

    Args:
        data: Objeto JSON con los siguientes campos:
            - function: Expresión matemática en términos de x. Ej: 'x**2', 'sin(x)'.
            - a: Límite inferior del intervalo de integración.
            - b: Límite superior del intervalo de integración.
            - n: Número de subintervalos. Debe ser par. Mayor valor = mayor precisión.
    Returns:
        Objeto JSON con los siguientes campos:
            - method: Método numérico utilizado (ej: "simpson-abierto").
            - function: Expresión integrada.
            - a: Límite inferior usado.
            - b: Límite superior usado.
            - n: Número de subintervalos usado.
            - result: Resultado aproximado de la integral.
    """
    f = _parse(data)
    result = _run(simpson_abierto, f, data.a, data.b, data.n)
    return IntegrationResponse(
        method="simpson-abierto", f=data.f, a=data.a, b=data.b, n=data.n, result=result
    )


@router.post("/simpson-1-3")
def simpson_1_3_endpoint(data: IntegrationRequest) -> IntegrationResponse:
    """
    Endpoint para calcular la integral definida de una función usando la regla de Simpson 1/3.
    Recibe una función como string, los límites de integración.
    Devuelve la aproximación numérica de la integral.

    Args:
        data: Objeto JSON con los siguientes campos:
            - function: Expresión matemática en términos de x. Ej: 'x**2', 'sin(x)'.
            - a: Límite inferior del intervalo de integración.
            - b: Límite superior del intervalo de integración.
            - n: Número de subintervalos. Debe ser igual a 2 para la regla de Simpson 1/3.
    Returns:
        Objeto JSON con los siguientes campos:
            - method: Método numérico utilizado (ej: "simpson-1-3").
            - function: Expresión integrada.
            - a: Límite inferior usado.
            - b: Límite superior usado.
            - n: Número de subintervalos usado (si aplica).
            - result: Resultado aproximado de la integral.
    """
    f = _parse(data)
    result = _run(simpson_1_3, f, data.a, data.b, data.n)
    return IntegrationResponse(
        method="simpson-1-3", f=data.f, a=data.a, b=data.b, n=data.n, result=result
    )


@router.post("/simpson-3-8")
def simpson_3_8_endpoint(data: IntegrationRequest) -> IntegrationResponse:
    """
    Endpoint para calcular la integral definida de una función usando la regla de Simpson 3/8.
    Recibe una función como string, los límites de integración y el número de subintervalos.
    Devuelve la aproximación numérica de la integral.

    Args:
        data: Objeto JSON con los siguientes campos:
            - function: Expresión matemática en términos de x. Ej: 'x**2', 'sin(x)'.
            - a: Límite inferior del intervalo de integración.
            - b: Límite superior del intervalo de integración.
            - n: Número de subintervalos. Debe ser igual a 3 para la regla de Simpson 3/8.
    Returns:
        Objeto JSON con los siguientes campos:
            - method: Método numérico utilizado (ej: "simpson-3-8").
            - function: Expresión integrada.
            - a: Límite inferior usado.
            - b: Límite superior usado.
            - n: Número de subintervalos usado (si aplica).
            - result: Resultado aproximado de la integral.
    """
    f = _parse(data)
    result = _run(simpson_3_8, f, data.a, data.b, data.n)
    return IntegrationResponse(
        method="simpson-3-8", f=data.f, a=data.a, b=data.b, n=data.n, result=result
    )
