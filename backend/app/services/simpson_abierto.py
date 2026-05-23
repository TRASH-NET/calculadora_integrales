from typing import Callable
from app.models.integration_models import IntegrationResult


def simpson_abierto(
    f: Callable[[float], float], a: float, b: float, n: int
) -> IntegrationResult:
    """
    Aproxima la integral definida de f en [a, b] usando la regla de Simpson
    abierto compuesta (patrón 1-4-2-4-2-...-4-1).

    Divide el intervalo en n subintervalos iguales (n debe ser par) y aplica
    el patrón de pesos de Simpson de forma compuesta:

        I = (h/3) · [f(x₁) + 4f(x₂) + 2f(x₃) + 4f(x₄) + ... + 4f(xₙ) + f(xₙ₊₁)]

    donde h = (b - a) / n.

    Los puntos se agrupan en paneles de 2 subintervalos cada uno. Dentro de
    cada panel k:
        - x₂ₖ   → peso 1 (extremo izquierdo, compartido con panel anterior)
        - x₂ₖ₊₁ → peso 4 (punto medio)
        - x₂ₖ₊₂ → peso 1 o 2 según sea extremo global o nodo compartido

    Error de truncamiento por panel:
        I - ∫f = -(1/90) · h⁵ · f⁽⁴⁾(ξ),   ξ ∈ [a, b]

    La regla es exacta para polinomios de grado ≤ 3.

    Args:
        f: Función a integrar. Debe aceptar un float y devolver un float.
        a: Límite inferior del intervalo de integración.
        b: Límite superior del intervalo de integración. Debe ser mayor que a.
        n: Número de subintervalos. Debe ser un número par positivo y no
           mayor a 10000.

    Returns:
        IntegrationResult con:
            - area: Aproximación numérica de ∫ f(x) dx en [a, b].
            - points: Lista de Point por panel (uno por cada par de subintervalos).

    Raises:
        ValueError: Si n no es par, si n ≤ 0, si n > 10000, o si a >= b.

    Example:
        >>> import math
        >>> simpson_abierto(math.sin, 0, math.pi, 100)
        # ≈ 2.0 con alta precisión
    """
    if n <= 0 or n > 10000:
        raise ValueError("n debe ser positivo y no mayor a 10000")

    if n % 2 != 0:
        raise ValueError(
            f"n debe ser par para la regla de Simpson abierto (se recibió n={n})"
        )

    if a >= b:
        raise ValueError("a debe ser menor que b")

    h = (b - a) / n

    x_vals = [a + i * h for i in range(n + 1)]
    y_vals = [f(x) for x in x_vals]

    points = []
    area = 0.0

    num_panels = n // 2

    for k in range(num_panels):
        i = 2 * k
        x_left, x_mid, x_right = x_vals[i], x_vals[i + 1], x_vals[i + 2]
        y_left, y_mid, y_right = y_vals[i], y_vals[i + 1], y_vals[i + 2]

        panel_area = (h / 3) * (y_left + 4 * y_mid + y_right)
        area += panel_area

        points.append(
            {
                "n": k + 1,
                "x": x_left,
                "y": y_left,
                "interval": f"[{round(x_left, 6)}, {round(x_right, 6)}]",
                "interval_area": panel_area,
            }
        )

    return IntegrationResult(area=area, points=points)
