import re
from sympy import symbols, sympify, lambdify, exp, log, sin, cos, tan, sqrt
from sympy.core.sympify import SympifyError
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)
from typing import Callable

x = symbols("x")

ALLOWED_NAMES = {
    "x": x,
    "exp": exp,
    "log": log,
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "sqrt": sqrt,
    "pi": __import__("sympy").pi,
    "e": __import__("sympy").E,
}

TRANSFORMATIONS = standard_transformations + (implicit_multiplication_application,)

# Caracteres permitidos en la expresión
VALID_CHARS = re.compile(r"^[a-zA-Z0-9\s\+\-\*\/\^\(\)\.\,\_]+$")


def parse_function(expression: str) -> Callable[[float], float]:
    """
    Parsea una expresión matemática en string y retorna una función callable.

    Validaciones aplicadas:
        - La expresión no puede estar vacía.
        - Solo se permiten caracteres matemáticos válidos.
        - Solo se permiten funciones y símbolos conocidos (whitelist).
        - La expresión debe ser parseable por sympy.
        - La función resultante debe ser evaluable en un punto de prueba.

    Args:
        expression: Expresión matemática en términos de x.
                    Ej: 'x**2', 'sin(x)', 'exp(x**2)', 'log(x)'.

    Returns:
        Función callable f(x: float) -> float.

    Raises:
        ValueError: Si la expresión es inválida, contiene símbolos no permitidos
                    o no puede evaluarse numéricamente.
    """
    if not expression or not expression.strip():
        raise ValueError("La expresión no puede estar vacía.")

    # Normalizar: convertir X -> x para evitar errores por mayúsculas
    expression = expression.replace("X", "x").strip()

    # Validar caracteres permitidos
    if not VALID_CHARS.match(expression):
        raise ValueError(
            f"La expresión contiene caracteres no permitidos: '{expression}'"
        )

    try:
        expr = parse_expr(
            expression,
            local_dict=ALLOWED_NAMES,
            transformations=TRANSFORMATIONS,
        )
    except (SympifyError, TypeError, SyntaxError) as e:
        raise ValueError(f"Expresión matemática inválida: '{expression}'. Detalle: {e}")

    # Verificar que no haya símbolos desconocidos (ej: palabras inventadas)
    free_symbols = expr.free_symbols - {x}
    if free_symbols:
        raise ValueError(
            f"La expresión contiene símbolos no reconocidos: "
            f"{', '.join(str(s) for s in free_symbols)}. "
            f"Solo se permite 'x' como variable."
        )

    f = lambdify(x, expr, modules=["math"])

    # Verificar que la función sea evaluable en un punto de prueba
    try:
        result = f(1.0)
        if result != result:  # NaN check
            raise ValueError("La función retorna NaN en x=1.")
    except ZeroDivisionError:
        # Puede ser válida en otros puntos (ej: 1/x evaluada en x=0)
        pass
    except Exception as e:
        raise ValueError(f"La función no puede evaluarse numéricamente: {e}")

    return f
