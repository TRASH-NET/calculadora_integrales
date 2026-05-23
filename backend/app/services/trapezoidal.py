from typing import Callable
from app.models.integration_models import IntegrationResult


def trapezoidal_rule(
    f: Callable[[float], float], a: float, b: float, n: int
) -> IntegrationResult:
    """
    Aproxima la integral definida de f en [a, b] usando la regla trapezoidal.

    La regla trapezoidal divide el intervalo [a, b] en n subintervalos iguales
    y aproxima el área bajo la curva como una suma de trapecios:

        ∫ f(x) dx ≈ (h/2) * [f(a) + 2·f(x₁) + 2·f(x₂) + ... + 2·f(xₙ₋₁) + f(b)]

    donde h = (b - a) / n es el ancho de cada subintervalo.

    Args:
        f: Función a integrar. Debe aceptar un float y devolver un float.
        a: Límite inferior del intervalo de integración.
        b: Límite superior del intervalo de integración. Debe ser mayor que a.
        n: Número de subintervalos (trapecios). Valores más altos dan mayor precisión.

    Returns:
        Aproximación numérica de la integral definida de f en [a, b].

    Raises:
        ValueError: Si n es menor o igual a cero, o si a >= b.

    Example:
        >>> import math
        >>> trapezoidal_rule(math.sin, 0, math.pi, 1000)
        1.9999983550656624  # ≈ 2.0 (valor exacto)
    """
    if n <= 0 or n > 10000:
        raise ValueError("n debe ser positivo y no mayor a 10000")

    if a >= b:
        raise ValueError("a debe ser menor que b")

    h = (b - a) / n

    x_vals = [a + i * h for i in range(n + 1)]
    y_vals = [f(x) for x in x_vals]

    points = []
    for i in range(n):
        x_i = x_vals[i]
        x_next = x_vals[i + 1]
        y_i = y_vals[i]
        y_next = y_vals[i + 1]

        points.append(
            {
                "n": i + 1,
                "x": x_i,
                "y": y_i,
                "interval": f"[{round(x_i, 6)}, {round(x_next, 6)}]",
                "interval_area": (h / 2) * (y_i + y_next),
            }
        )

    area = (h / 2) * (y_vals[0] + 2 * sum(y_vals[1:-1]) + y_vals[-1])

    return IntegrationResult(area=area, points=points)
