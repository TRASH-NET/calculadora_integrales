import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import type { EndpointKey } from "@/constants/integration.constants";
import { ENDPOINTS } from "@/constants/integration.constants";


interface IntegrationFormProps {
    formData: {
        endpoint: EndpointKey
        f: string
        a: number
        b: number
        n: number
    }
    loading: boolean
    onchange: <K extends keyof IntegrationFormProps["formData"]>(
        field: K,
        value: IntegrationFormProps["formData"][K]
    ) => void
    onCalculate: () => void
}

export function IntegrationForm({
    formData,
    loading,
    onchange,
    onCalculate,
}: IntegrationFormProps) {

    const endpointOptions = Object.keys(ENDPOINTS) as EndpointKey[];
    const formatEndpointLabel = (key: EndpointKey) => {
        switch (key) {
            case "trapezoidal":
                return "Metodo Trapezoidal";
            case "boole":
                return "Metodo de Jorge Boole";
            case "simpson_abierto":
                return "Metodo de Simpson Abierto";
            case "simpson_1_3":
                return "Metodo de Simpson 1/3";
            case "simpson_3_8":
                return "Metodo de Simpson 3/8";
            default:
                return key;
        }
    }

    return (
        <div className="flex flex-col gap-6">

            <div className="flex flex-col gap-1">
                <h2 className="text-2xl font-bold tracking-tight text-white">
                    Calculadora de Integrales
                </h2>
                <p className="text-sm text-slate-400">
                    Configura los parametros y haz click en "Calcular" para ver el resultado y la gráfica aquí
                </p>
            </div>

            {/* Método */}
            <div className="flex flex-col gap-2">
                <Label className="text-slate-300">Metodo</Label>
                <Select
                    value={formData.endpoint}
                    onValueChange={(value) => onchange("endpoint", value as EndpointKey)}
                >
                    <SelectTrigger className="bg-slate-800 border-slate-700 text-white">
                        <SelectValue placeholder="Select a method" />
                    </SelectTrigger>
                    <SelectContent className="bg-slate-800 border-slate-700 text-white">
                        {endpointOptions.map((key) => (
                            <SelectItem key={key} value={key}>
                                {formatEndpointLabel(key)}
                            </SelectItem>
                        ))}
                    </SelectContent>
                </Select>
            </div>

            {/* Función */}
            <div className="flex flex-col gap-2">
                <Label className="text-slate-300">Funcion f(x)</Label>
                <Input
                    value={formData.f}
                    onChange={(e) => onchange("f", e.target.value)}
                    placeholder="e.g. x**2, sin(x)"
                    className="bg-slate-800 border-slate-700 text-white placeholder:text-slate-500"
                />
            </div>

            {/* Límites */}
            <div className="flex gap-4">
                <div className="flex flex-col gap-2 flex-1">
                    <Label className="text-slate-300">Limite inferior (a)</Label>
                    <Input
                        type="number"
                        value={formData.a}
                        onChange={(e) => onchange("a", Number(e.target.value))}
                        className="bg-slate-800 border-slate-700 text-white"
                    />
                </div>
                <div className="flex flex-col gap-2 flex-1">
                    <Label className="text-slate-300">Limite superior (b)</Label>
                    <Input
                        type="number"
                        value={formData.b}
                        onChange={(e) => onchange("b", Number(e.target.value))}
                        className="bg-slate-800 border-slate-700 text-white"
                    />
                </div>
            </div>

            {/* Subintervalos */}
            <div className="flex flex-col gap-2">
                <Label className="text-slate-300">Subintervalos (n)</Label>
                <Input
                    type="number"
                    value={formData.n}
                    onChange={(e) => onchange("n", Number(e.target.value))}
                    min={1}
                    className="bg-slate-800 border-slate-700 text-white"
                />
            </div>

            <Button
                onClick={onCalculate}
                disabled={loading}
                className="w-full bg-indigo-600 hover:bg-indigo-500 text-white font-semibold"
            >
                {loading ? "Calculando..." : "Calcular"}
            </Button>

        </div>
    )
}