import { useState } from 'react';

const steps = ['Basic Information', 'Symptoms', 'Health Data', 'Voice', 'Camera', 'Motion Sensors', 'Data Quality', 'AI Analysis', 'Result'];

export default function ScreeningPage() {
  const [activeStep, setActiveStep] = useState(1);

  return (
    <div className="space-y-8">
      <div className="glass rounded-3xl p-6">
        <div className="flex items-center justify-between mb-6">
          <div>
            <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">Patient Screening</p>
            <h2 className="text-3xl font-bold mt-2">Guided workflow</h2>
          </div>
          <div className="rounded-full border border-cyan-400/30 bg-cyan-400/5 px-3 py-1.5 text-sm text-cyan-200">Demo / Research Data</div>
        </div>

        <div className="grid gap-3 md:grid-cols-9">
          {steps.map((step, index) => (
            <button key={step} onClick={() => setActiveStep(index + 1)} className={`rounded-2xl border px-3 py-3 text-left text-xs ${activeStep === index + 1 ? 'border-cyan-400 bg-cyan-500/10 text-cyan-100' : 'border-slate-700 bg-slate-900/60 text-slate-300'}`}>
              {index + 1}. {step}
            </button>
          ))}
        </div>
      </div>

      <div className="grid lg:grid-cols-[1.1fr_0.9fr] gap-6">
        <div className="glass rounded-3xl p-6">
          <h3 className="text-xl font-semibold mb-4">Symptoms</h3>
          <div className="grid md:grid-cols-2 gap-4">
            <label className="text-sm">
              <span className="text-slate-300 block mb-2">Symptom name</span>
              <input className="w-full rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-white" placeholder="Fatigue" />
            </label>
            <label className="text-sm">
              <span className="text-slate-300 block mb-2">Severity (0-10)</span>
              <input type="number" min={0} max={10} className="w-full rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-white" defaultValue={4} />
            </label>
            <label className="text-sm">
              <span className="text-slate-300 block mb-2">Duration</span>
              <input className="w-full rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-white" placeholder="7 days" />
            </label>
            <label className="text-sm">
              <span className="text-slate-300 block mb-2">Frequency</span>
              <select className="w-full rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-white">
                <option>Occasional</option>
                <option>Frequent</option>
                <option>Persistent</option>
              </select>
            </label>
            <label className="text-sm md:col-span-2">
              <span className="text-slate-300 block mb-2">Notes</span>
              <textarea className="w-full rounded-xl border border-slate-700 bg-slate-950/60 px-3 py-2 text-white" rows={4} placeholder="Optional notes" />
            </label>
          </div>
        </div>

        <div className="glass rounded-3xl p-6">
          <h3 className="text-xl font-semibold mb-4">Data Quality</h3>
          <div className="space-y-3">
            {['Missing Values', 'Invalid Values', 'Duplicates', 'Outliers', 'Noise', 'Leakage', 'Signal Quality'].map((item) => (
              <div key={item} className="flex items-center justify-between rounded-xl border border-slate-700 bg-slate-900/60 px-3 py-2 text-sm">
                <span>{item}</span>
                <span className="text-cyan-300">Pass</span>
              </div>
            ))}
          </div>
          <button className="button-primary mt-6 w-full">Run AI Analysis</button>
        </div>
      </div>
    </div>
  );
}
