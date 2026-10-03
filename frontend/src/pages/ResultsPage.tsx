export default function ResultsPage() {
  return (
    <div className="glass rounded-3xl p-8">
      <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">Multimodal Screening Result</p>
      <h2 className="mt-3 text-3xl font-bold">Risk Category</h2>
      <div className="mt-5 grid md:grid-cols-2 gap-6 text-sm text-slate-300">
        <div className="rounded-2xl border border-slate-700 bg-slate-900/60 p-4"><strong>Model:</strong> Hybrid QML</div>
        <div className="rounded-2xl border border-slate-700 bg-slate-900/60 p-4"><strong>Reliability:</strong> Reliable Enough for Screening</div>
        <div className="rounded-2xl border border-slate-700 bg-slate-900/60 p-4"><strong>Data Quality:</strong> Acceptable</div>
        <div className="rounded-2xl border border-slate-700 bg-slate-900/60 p-4"><strong>Signal Agreement:</strong> Moderate</div>
      </div>
      <div className="mt-6 rounded-2xl border border-cyan-400/30 bg-cyan-500/10 p-5 text-cyan-100">
        An elevated risk pattern was detected. Further evaluation by a qualified healthcare professional is recommended.
      </div>
      <p className="mt-4 text-slate-300">This is a research/decision-support screening result and is not a medical diagnosis.</p>
    </div>
  );
}
