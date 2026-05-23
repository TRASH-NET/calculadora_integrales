import { useIntegration } from "./hooks/useIntegration"
import { IntegralChart } from "./components/IntegralChart"
import { ResultCard } from "./components/ResultCard"
import { IntegrationForm } from "./components/forms/IntegrationForm";
import { IntegrationTable } from './components/IntegrationTable';

export default function App() {

	const { formData, result, error, loading, handleChange, calculate } = useIntegration()

	return (
		<div className="min-h-screen bg-slate-900 text-white p-8">

			<div className="max-w-7xl mx-auto flex flex-col gap-6">

				{/* Main layout */}
				<div className="flex gap-8 flex-col lg:flex-row">

					{/* Columna izquierda — formulario */}
					<div className="w-full lg:w-1/4 shrink-0 flex flex-col gap-4">
						<IntegrationForm
							formData={formData}
							loading={loading}
							onchange={handleChange}
							onCalculate={calculate}
						/>
						{result && <ResultCard result={result} />}


						{/* Error */}
						{error && (
							<p className="text-sm text-red-400 bg-red-950 border border-red-800 rounded-md px-4 py-3">
								{error}
							</p>
						)}
					</div>

					{/* Columna derecha — resultado y gráfica */}
					<div className="w-full flex-1 flex flex-col gap-4 h-full">
						{result ? (
							<>
								<IntegralChart
									points={result.result.points}
									a={result.a}
									b={result.b}
								/>
								<IntegrationTable points={result.result.points} />
							</>
						) : (
							<div className="flex-1 flex items-center justify-center border border-dashed border-slate-700 rounded-xl min-h-96">
								<p className="text-slate-500 text-sm">
									Configura los parametros y haz click en "Calcular" para ver el resultado y la gráfica aquí
								</p>
							</div>
						)}
					</div>

				</div>

			</div>

		</div>
	)
}