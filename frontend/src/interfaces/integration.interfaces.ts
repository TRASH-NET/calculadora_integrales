export interface Point {
    n: number
    x: number
    y: number
    interval: string
    interval_area: number
}

export interface IntegrationResult {
    area: number
    points: Point[]
}

export interface IntegrationRequest {
    f: string
    a: number
    b: number
    n: number
}

export interface IntegrationResponse {
    method: string
    f: string
    a: number
    b: number
    n: number
    result: IntegrationResult
}