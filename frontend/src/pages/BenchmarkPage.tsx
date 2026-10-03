import { BarChart, Bar, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const data = [
  { name: 'Classical ML', accuracy: 84 },
  { name: 'Quantum ML', accuracy: 86 },
  { name: 'Hybrid QML', accuracy: 91 },
];

export default function BenchmarkPage() {
  return (
    <div className="space-y-8">
      <div className="glass rounded-3xl p-6">
        <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">Benchmark Center</p>
        <h2 className="text-3xl font-bold mt-3">QUANTUM ADVANTAGE REALITY CHECK</h2>
      </div>

      <div className="glass rounded-3xl p-6">
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
              <XAxis dataKey="name" stroke="#cbd5e1" />
              <YAxis stroke="#cbd5e1" domain={[0, 100]} />
              <Tooltip />
              <Bar dataKey="accuracy" fill="#67e8f9" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="grid md:grid-cols-3 gap-6">
        {['Classical ML', 'Quantum ML', 'Hybrid QML'].map((model) => (
          <div key={model} className="glass rounded-3xl p-6">
            <h3 className="text-xl font-semibold">{model}</h3>
            <div className="mt-4 space-y-2 text-sm text-slate-300">
              <div className="flex justify-between"><span>Accuracy</span><span>0.91</span></div>
              <div className="flex justify-between"><span>Recall</span><span>0.88</span></div>
              <div className="flex justify-between"><span>ROC-AUC</span><span>0.90</span></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
