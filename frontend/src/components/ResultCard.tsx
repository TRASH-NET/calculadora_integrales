import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import type { IntegrationResponse } from "../interfaces/integration.interfaces"

interface ResultCardProps {
    result: IntegrationResponse
}

export function ResultCard({ result }: ResultCardProps) {
    return (
        <Card className="bg-slate-800 border-slate-700">
            <CardHeader className="pb-3">
                <CardTitle className="text-slate-400 text-sm font-medium uppercase tracking-widest">
                    Resultado
                </CardTitle>
            </CardHeader>

            <CardContent className="space-y-6">
                {/* Área Principal */}
                <div>
                    <p className="text-6xl font-bold text-white tracking-tighter">
                        {result.result.area.toFixed(4)}
                    </p>
                    <p className="text-xs text-slate-500 mt-1">ÁREA CALCULADA</p>
                </div>

                {/* Información detallada */}
                <div className="grid grid-cols-2 gap-x-8 gap-y-4 text-sm">
                    <div className="flex flex-col">
                        <span className="text-slate-500 text-xs font-medium uppercase tracking-wider">Método</span>
                        <span className="text-slate-200 font-medium">{result.method}</span>
                    </div>

                    <div className="flex flex-col">
                        <span className="text-slate-500 text-xs font-medium uppercase tracking-wider">f(x)</span>
                        <span className="text-slate-200 font-medium font-mono">{result.f}</span>
                    </div>

                    <div className="flex flex-col">
                        <span className="text-slate-500 text-xs font-medium uppercase tracking-wider">Límite inferior(a)</span>
                        <span className="text-slate-200 font-medium">{result.a}</span>
                    </div>

                    <div className="flex flex-col">
                        <span className="text-slate-500 text-xs font-medium uppercase tracking-wider">Límite superior(b)</span>
                        <span className="text-slate-200 font-medium">{result.b}</span>
                    </div>

                    <div className="flex flex-col">
                        <span className="text-slate-500 text-xs font-medium uppercase tracking-wider">Subintervalos(n)</span>
                        <span className="text-slate-200 font-medium">{result.n}</span>
                    </div>
                </div>
            </CardContent>
        </Card>
    )
}