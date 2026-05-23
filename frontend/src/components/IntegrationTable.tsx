import type { Point } from "../interfaces/integration.interfaces"

interface IntegrationTableProps {
    points: Point[]
}

export function IntegrationTable({ points }: IntegrationTableProps) {
    return (
        <div className="overflow-auto rounded-lg border border-slate-700 max-h-85">
            <table className="w-full text-sm text-left">
                <thead className="sticky top-0 bg-slate-800 text-slate-400 uppercase text-xs tracking-widest">
                    <tr>
                        <th className="px-4 py-3">n</th>
                        <th className="px-4 py-3">x</th>
                        <th className="px-4 py-3">f(x)</th>
                        <th className="px-4 py-3">Intervalo</th>
                        <th className="px-4 py-3">Area</th>
                    </tr>
                </thead>
                <tbody>
                    {points.map((p) => (
                        <tr
                            key={p.n}
                            className="border-t border-slate-700 hover:bg-slate-800 transition-colors"
                        >
                            <td className="px-4 py-2 text-slate-400">{p.n}</td>
                            <td className="px-4 py-2 text-white">{p.x.toFixed(6)}</td>
                            <td className="px-4 py-2 text-white">{p.y.toFixed(6)}</td>
                            <td className="px-4 py-2 text-indigo-400 font-mono">{p.interval}</td>
                            <td className="px-4 py-2 text-emerald-400">{p.interval_area.toFixed(6)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}