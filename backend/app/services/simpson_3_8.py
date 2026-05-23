from typing import Callable
from app.models.integration_models import IntegrationResult, Point


def simpson_3_8(
    f: Callable[[float], float], a: float, b: float, n: int
) -> IntegrationResult:
    """
    Aproxima la integral definida de f en [a, b] usando la regla de Simpson 3/8.

    La regla de Simpson 3/8 es una regla de Newton-Cotes de orden 3 que interpola
    f con un polinomio de grado 3 sobre 4 puntos equiespaciados:

        I = (3h/8) · [f(x₁) + 3f(x₂) + 3f(x₃) + f(x₄)]

    donde h = (b - a) / 3 es el ancho de cada subintervalo.

    Error de truncamiento:
        I - ∫f = -(3/80) · h⁵ · f⁽⁴⁾(ξ),   ξ ∈ [a, b]

    La regla es exacta para polinomios de grado ≤ 3.

    Args:
        f: Función a integrar. Debe aceptar un float y devolver un float.
        a: Límite inferior del intervalo de integración.
        b: Límite superior del intervalo de integración. Debe ser mayor que a.
        n: Número de subintervalos. Debe ser igual a 3 para la regla de Simpson 3/8.

    Returns:
        IntegrationResult con:
            - area: Aproximación numérica de ∫ f(x) dx en [a, b].
            - points: Lista con los 3 intervalos evaluados.

    Raises:
        ValueError: Si a >= b.

    Example:
        >>> import math
        >>> simpson_3_8(math.sin, 0, math.pi)
        # ≈ 2.0 con buena precisión
    """
    if a >= b:
        raise ValueError("a debe ser menor que b")

    if n != 3:
        raise ValueError("n debe ser igual a 3 para la regla de Simpson 3/8")

    h = (b - a) / 3

    x0, x1, x2, x3 = a, a + h, a + 2 * h, b
    y0, y1, y2, y3 = f(x0), f(x1), f(x2), f(x3)

    area = (3 * h / 8) * (y0 + 3 * y1 + 3 * y2 + y3)

    points = [
        Point(
            n=1,
            x=x0,
            y=y0,
            interval=f"[{round(x0, 6)}, {round(x1, 6)}]",
            interval_area=(3 * h / 8) * y0,  # peso 1
        ),
        Point(
            n=2,
            x=x1,
            y=y1,
            interval=f"[{round(x1, 6)}, {round(x2, 6)}]",
            interval_area=(3 * h / 8) * 3 * y1,  # peso 3
        ),
        Point(
            n=3,
            x=x2,
            y=y2,
            interval=f"[{round(x2, 6)}, {round(x3, 6)}]",
            interval_area=(3 * h / 8) * 3 * y2,  # peso 3
        ),
        Point(
            n=4,
            x=x3,
            y=y3,
            interval=f"[{round(x3, 6)}, {round(x3, 6)}]",
            interval_area=(3 * h / 8) * y3,  # peso 1
        ),
    ]

    return IntegrationResult(area=area, points=points)
