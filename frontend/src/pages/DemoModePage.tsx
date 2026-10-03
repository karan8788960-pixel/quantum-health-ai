export default function DemoModePage() {
  return (
    <div className="glass rounded-3xl p-8">
      <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">SIH Demo Mode</p>
      <h2 className="mt-3 text-3xl font-bold">Start Demo</h2>
      <div className="mt-6 space-y-3 text-slate-300">
        {['Symptoms', 'Voice', 'Camera', 'Motion Sensors', 'Data Quality', 'Feature Engineering', 'Classical ML', 'QML', 'Hybrid QML', 'Benchmark', 'Explainability', 'Reliability', 'Final Result', 'Research Report'].map((step) => (
          <div key={step} className="rounded-2xl border border-slate-700 bg-slate-900/60 p-3">{step}</div>
        ))}
      </div>
      <div className="mt-6 rounded-2xl border border-yellow-400/30 bg-yellow-500/10 p-4 text-yellow-200">DEMO / RESEARCH DATA</div>
    </div>
  );
}
