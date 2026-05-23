import type { EndpointKey } from "../constants/integration.constants";
import type { IntegrationRequest, IntegrationResponse } from "../interfaces/integration.interfaces";

import { ENDPOINTS } from "../constants/integration.constants";

/**
 * Calcula una integral numérica usando el método especificado.
 *
 * @param endpoint - Método numérico a utilizar (ej: "trapezoidal")
 * @param request - Parámetros de la integración (función, límites, subintervalos)
 *
 * @returns Resultado de la integración con área y puntos evaluados
 *
 * @throws Error cuando el endpoint no existe o la API responde con error
 */


export const calculateIntegral = async (
    endpoint: EndpointKey,
    request: IntegrationRequest
): Promise<IntegrationResponse> => {


    const url = ENDPOINTS[endpoint];

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(request)
    })

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Error calculating integral');

    }

    return response.json();
}