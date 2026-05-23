export const BASE_URL = import.meta.env.VITE_BASE_URL;

export const ENDPOINTS = {
    trapezoidal: `${BASE_URL}trapezoidal/`,
    boole: `${BASE_URL}boole/`,
    simpson_abierto: `${BASE_URL}simpson-abierto/`,
    simpson_1_3: `${BASE_URL}simpson-1-3/`,
    simpson_3_8: `${BASE_URL}simpson-3-8/`,
} as const;

export type EndpointKey = keyof typeof ENDPOINTS;