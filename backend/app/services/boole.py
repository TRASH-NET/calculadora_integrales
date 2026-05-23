from typing import Callable
from app.models.integration_models import IntegrationResult


def boole_rule(
    f: Callable[[float], float], a: float, b: float, n: int
) -> IntegrationResult:
    """
    Aproxima la integral definida de f en [a, b] usando la regla de Boole
    (Newton-Cotes de orden 4).

    La regla de Boole es una regla de Newton-Cotes que se obtiene interpolando
    con un polinomio de grado 4 sobre 5 puntos equiespaciados. Para un único
    panel de 4 subintervalos, la fórmula es:

        I₄f = (2h/45) · [7f(x₀) + 32f(x₁) + 12f(x₂) + 32f(x₃) + 7f(x₄)]

    donde h = (b - a) / 4 es el ancho de cada subintervalo.

    Para aplicarla sobre [a, b] con n paneles (n debe ser múltiplo de 4), se
    divide el intervalo en n subintervalos de ancho h = (b - a) / n y se
    aplica la fórmula compuesta:

        ∫ f(x) dx ≈ (2h/45) · Σₖ [7f(x₄ₖ) + 32f(x₄ₖ₊₁) + 12f(x₄ₖ₊₂)
                                    + 32f(x₄ₖ₊₃) + 7f(x₄ₖ₊₄)]

    sumando sobre cada panel k = 0, 1, …, (n/4 - 1). Los nodos interiores
    compartidos entre paneles adyacentes se acumulan correctamente.

    Error de la regla de Boole (panel simple):
        I₄f - ∫f = (8/945) · h⁷ · f⁽⁶⁾(ξ),   ξ ∈ [a, b]

    El error es de orden O(h⁷) por panel, lo que hace a esta regla exacta para
    polinomios de grado ≤ 5.

    Args:
        f: Función a integrar. Debe aceptar un float y devolver un float.
        a: Límite inferior del intervalo de integración.
        b: Límite superior del intervalo de integración. Debe ser mayor que a.
        n: Número de subintervalos. Debe ser un múltiplo positivo de 4 y no
           mayor a 10000. Valores más altos dan mayor precisión.

    Returns:
        IntegrationResult con:
            - area: Aproximación numérica de ∫ f(x) dx en [a, b].
            - points: Lista de dicts con información de cada panel, incluyendo
              los 5 nodos, sus evaluaciones y el aporte de área de ese panel.

    Raises:
        ValueError: Si n no es un múltiplo de 4, si n ≤ 0, si n > 10000,
                    o si a >= b.

    Example:
        >>> import math
        >>> boole_rule(math.sin, 0, math.pi, 4)
        # ≈ 2.0001095 (exacto: 2.0)
        >>> boole_rule(math.sin, 0, math.pi, 1000)
        # ≈ 2.0 con alta precisión
    """
    if n <= 0 or n > 10000:
        raise ValueError("n debe ser positivo y no mayor a 10000")

    if n % 4 != 0:
        raise ValueError(
            f"n debe ser múltiplo de 4 para la regla de Boole (se recibió n={n})"
        )

    if a >= b:
        raise ValueError("a debe ser menor que b")

    h = (b - a) / n

    # Nodos y evaluaciones globales
    x_vals = [a + i * h for i in range(n + 1)]
    y_vals = [f(x) for x in x_vals]

    # Pesos de la regla de Boole dentro de cada panel: [7, 32, 12, 32, 7]
    boole_weights = [7, 32, 12, 32, 7]

    points = []
    area = 0.0

    num_panels = n // 4

    for k in range(num_panels):
        # Índices de los 5 nodos del panel k
        idx = [4 * k + j for j in range(5)]

        panel_x = [x_vals[i] for i in idx]
        panel_y = [y_vals[i] for i in idx]

        # Área del panel: (2h/45) · [7y₀ + 32y₁ + 12y₂ + 32y₃ + 7y₄]
        panel_area = (2 * h / 45) * sum(boole_weights[j] * panel_y[j] for j in range(5))
        area += panel_area

        points.append(
            {
                "n": k + 1,
                "x": panel_x[0],
                "y": panel_y[0],
                "interval": f"[{round(panel_x[0], 6)}, {round(panel_x[4], 6)}]",
                "interval_area": panel_area,
            }
        )

    return IntegrationResult(area=area, points=points)
