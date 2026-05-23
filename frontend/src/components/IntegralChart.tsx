import {
    Area,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
    Bar,
    ComposedChart,
} from "recharts"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import type { Point } from "../interfaces/integration.interfaces"

interface IntegralChartProps {
    points: Point[]
    a: number
    b: number
}

export function IntegralChart({ points, a, b }: IntegralChartProps) {

    const visiblePoints = points.filter(
        (p) => p.x >= a && p.x <= b
    )

    // ancho de intervalo
    const dx =
        visiblePoints.length > 1
            ? visiblePoints[1].x - visiblePoints[0].x
            : 1

    return (
        <Card className="bg-slate-800 border-slate-700 h-full">
            <CardHeader className="pb-2">
                <CardTitle className="text-slate-400 text-sm font-medium uppercase tracking-widest">
                    Grafico
                </CardTitle>
            </CardHeader>

            <CardContent>
                <ResponsiveContainer width="100%" height={350}>
                    <ComposedChart
                        data={visiblePoints}
                        margin={{ top: 10, right: 20, left: 0, bottom: 0 }}
                    >

                        <defs>
                            <linearGradient id="integralGradient" x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor="#6366f1" stopOpacity={0.4} />
                                <stop offset="95%" stopColor="#6366f1" stopOpacity={0} />
                            </linearGradient>
                        </defs>

                        <CartesianGrid strokeDasharray="3 3" stroke="#334155" />

                        <XAxis
                            dataKey="x"
                            stroke="#64748b"
                            tick={{ fill: "#94a3b8", fontSize: 12 }}
                            tickFormatter={(v) => Number(v).toFixed(2)}
                        />

                        <YAxis
                            stroke="#64748b"
                            tick={{ fill: "#94a3b8", fontSize: 12 }}
                            tickFormatter={(v) => Number(v).toFixed(2)}
                        />

                        <Tooltip
                            cursor={{
                                stroke: "#6366f1",
                                strokeWidth: 1,
                                strokeDasharray: "4 4",
                            }}
                            content={({ active, payload }) => {

                                if (!active || !payload || payload.length === 0) {
                                    return null
                                }

                                const point = payload[0].payload as Point

                                return (
                                    <div
                                        className="
                    rounded-xl border border-slate-700
                    bg-slate-900/95 backdrop-blur-sm
                    px-4 py-3 shadow-2xl
                "
                                    >
                                        <div className="flex flex-col gap-1 text-sm">

                                            <div className="flex items-center gap-2">
                                                <span className="text-slate-400">x:</span>

                                                <span className="font-mono text-white">
                                                    {point.x.toFixed(6)}
                                                </span>
                                            </div>

                                            <div className="flex items-center gap-2">
                                                <span className="text-slate-400">y:</span>

                                                <span className="font-mono text-indigo-400">
                                                    {point.y.toFixed(6)}
                                                </span>
                                            </div>

                                            <div className="flex items-center gap-2">
                                                <span className="text-slate-400">area:</span>

                                                <span className="font-mono text-emerald-400">
                                                    {point.interval_area.toFixed(6)}
                                                </span>
                                            </div>

                                            <div className="mt-2 border-t border-slate-700 pt-2">
                                                <span className="text-xs text-slate-500">
                                                    intervalo {point.interval}
                                                </span>
                                            </div>

                                        </div>
                                    </div>
                                )
                            }}
                        />

                        {/* RECTANGULOS DE APROXIMACION */}
                        <Bar
                            dataKey="y"
                            fill="#10b981"
                            fillOpacity={0.25}
                            stroke="#10b981"
                            strokeOpacity={0.5}
                            barSize={dx * 3}
                        />

                        {/* FUNCION ORIGINAL */}
                        <Area
                            type="monotone"
                            dataKey="y"
                            stroke="#6366f1"
                            strokeWidth={2}
                            fill="url(#integralGradient)"
                            dot={false}
                            activeDot={{
                                r: 6,
                                fill: "#6366f1",
                                stroke: "#fff",
                                strokeWidth: 2,
                            }}
                        />
                    </ComposedChart>
                </ResponsiveContainer>
            </CardContent>
        </Card>
    )
}