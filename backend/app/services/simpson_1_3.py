from typing import Callable
from app.models.integration_models import IntegrationResult, Point


def simpson_1_3(
    f: Callable[[float], float], a: float, b: float, n: int
) -> IntegrationResult:
    """
    Aproxima la integral definida de f en [a, b] usando la regla de Simpson 1/3.

    La regla de Simpson 1/3 es una regla de Newton-Cotes de orden 2 que interpola
    f con un polinomio de grado 2 sobre 3 puntos equiespaciados:

        I = (h/3) · [f(x₁) + 4f(x₂) + f(x₃)]

    donde h = (b - a) / 2 es el ancho de cada subintervalo.

    Error de truncamiento:
        I - ∫f = -(1/90) · h⁵ · f⁽⁴⁾(ξ),   ξ ∈ [a, b]

    La regla es exacta para polinomios de grado ≤ 3.

    Args:
        f: Función a integrar. Debe aceptar un float y devolver un float.
        a: Límite inferior del intervalo de integración.
        b: Límite superior del intervalo de integración. Debe ser mayor que a.

    Returns:
        IntegrationResult con:
            - area: Aproximación numérica de ∫ f(x) dx en [a, b].
            - points: Lista con los 2 intervalos evaluados.

    Raises:
        ValueError: Si a >= b.

    Example:
        >>> import math
        >>> simpson_1_3(math.sin, 0, math.pi)
        # ≈ 2.0944 (exacto: 2.0)
    """
    if a >= b:
        raise ValueError("a debe ser menor que b")
    if n != 2:
        raise ValueError("n debe ser igual a 2 para la regla de Simpson 1/3")

    h = (b - a) / 2
    x0, x1, x2 = a, a + h, b
    y0, y1, y2 = f(x0), f(x1), f(x2)
    area = (h / 3) * (y0 + 4 * y1 + y2)

    points = [
        Point(
            n=1,
            x=x0,
            y=y0,
            interval=f"[{round(x0, 6)}, {round(x1, 6)}]",
            interval_area=(h / 3) * y0,  # peso 1
        ),
        Point(
            n=2,
            x=x1,
            y=y1,
            interval=f"[{round(x1, 6)}, {round(x2, 6)}]",
            interval_area=(h / 3) * 4 * y1,  # peso 4
        ),
        Point(
            n=3,
            x=x2,
            y=y2,
            interval=f"[{round(x2, 6)}, {round(x2, 6)}]",
            interval_area=(h / 3) * y2,  # peso 1
        ),
    ]

    return IntegrationResult(area=area, points=points)
