from pydantic import BaseModel, Field


class Point(BaseModel):
    n: int = Field(description="Índice del subintervalo o panel.")
    x: float = Field(description="Valor de x izquierdo del intervalo.")
    y: float = Field(description="Valor de f(x).")
    interval: str = Field(description="Rango del intervalo. Ej: [0.0, 0.5]")
    interval_area: float = Field(description="Área del intervalo.")


class IntegrationResult(BaseModel):
    area: float = Field(description="Resultado aproximado de la integral.")
    points: list[Point] = Field(
        description="Lista de puntos evaluados durante la integración. Cada punto tiene un valor de x y su correspondiente f(x)."
    )


class IntegrationRequest(BaseModel):
    f: str = Field(
        description="Expresión matemática en términos de x. Ej: 'x**2', 'sin(x)'.",
        examples=["x**2", "sin(x)", "x**3 - 2*x + 1"],
    )
    a: float = Field(description="Límite inferior del intervalo de integración.")
    b: float = Field(description="Límite superior del intervalo de integración.")
    n: int = Field(
        description="Número de subintervalos (trapecios). Mayor valor = mayor precisión.",
    )


class IntegrationResponse(BaseModel):
    method: str = Field(
        description="Método numérico utilizado.",
        examples=["trapezoidal"],
    )
    f: str = Field(description="Expresión integrada.")
    a: float = Field(description="Límite inferior usado.")
    b: float = Field(description="Límite superior usado.")
    n: int = Field(description="Número de subintervalos usado.")
    result: IntegrationResult = Field(
        description="Resultado de la integración, incluyendo puntos evaluados."
    )
