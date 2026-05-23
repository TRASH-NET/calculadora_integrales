import { useState } from "react";

import type { EndpointKey } from "../constants/integration.constants";
import type { IntegrationResponse } from "../interfaces/integration.interfaces";

import { calculateIntegral } from "../api/integration";

interface FormData {
    endpoint: EndpointKey
    f: string
    a: number
    b: number
    n: number
}

const INITIAL_FORM: FormData = {
    endpoint: 'trapezoidal',
    f: "x**2",
    a: 0,
    b: 2,
    n: 1000,
}

export function useIntegration() {

    const [formData, setFormData] = useState<FormData>(INITIAL_FORM);
    const [result, setResult] = useState<IntegrationResponse | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(false);

    const handleChange = <K extends keyof FormData>(field: K, value: FormData[K]): void => {
        setFormData((prev) => ({
            ...prev,
            [field]: value
        }))
    }

    const calculate = async (): Promise<void> => {
        setLoading(true);
        setError(null);
        setResult(null);

        const { endpoint, ...request } = formData;

        try {
            const data = await calculateIntegral(endpoint, request);
            setResult(data);
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Error desconocido');
        } finally {
            setLoading(false);
        }
    }

    return {
        formData,
        result,
        error,
        loading,
        handleChange,
        calculate
    }
}