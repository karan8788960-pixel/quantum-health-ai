export default function ReportsPage() {
  return (
    <div className="glass rounded-3xl p-8">
      <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">Reports</p>
      <h2 className="mt-3 text-3xl font-bold">Research report generator</h2>
      <div className="mt-6 grid md:grid-cols-2 gap-6 text-sm text-slate-300">
        {['Dataset', 'Preprocessing', 'Feature engineering', 'Feature selection', 'Classical model', 'QML model', 'Hybrid model', 'Metrics', 'Explainability', 'Robustness', 'Fairness', 'Reliability'].map((section) => (
          <div key={section} className="rounded-2xl border border-slate-700 bg-slate-900/60 p-4">{section}</div>
        ))}
      </div>
      <button className="button-primary mt-8">Export PDF</button>
    </div>
  );
}
