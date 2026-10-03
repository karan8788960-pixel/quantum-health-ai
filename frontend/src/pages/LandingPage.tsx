import { motion } from 'framer-motion';
import { ArrowRight, Activity, BrainCircuit, ShieldCheck, Sparkles } from 'lucide-react';
import { Link } from 'react-router-dom';

const steps = ['Symptoms', 'Voice', 'Vision', 'Motion Sensors', 'Feature Engineering', 'Classical ML + QML', 'Explainable Risk Assessment'];

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-midnight text-slate-100">
      <header className="section-shell pt-8 pb-4">
        <nav className="glass rounded-full px-5 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="h-9 w-9 rounded-full bg-gradient-to-br from-cyan-300 to-violet-500 flex items-center justify-center text-sm font-bold text-slate-950">Q</div>
            <div>
              <div className="font-semibold">Quantum Health AI</div>
            </div>
          </div>
          <div className="hidden md:flex items-center gap-6 text-sm text-slate-300">
            <a href="#problem">Problem</a>
            <a href="#solution">Solution</a>
            <a href="#benchmarking">Benchmarking</a>
            <a href="#how-it-works">How It Works</a>
          </div>
          <div className="flex gap-3">
            <Link to="/screening" className="button-primary">Start Screening</Link>
          </div>
        </nav>
      </header>

      <main>
        <section className="section-shell py-12 md:py-20">
          <div className="grid lg:grid-cols-[1.2fr_0.8fr] items-center gap-10">
            <div>
              <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="inline-flex items-center gap-2 rounded-full border border-cyan-400/30 bg-cyan-400/5 px-3 py-1.5 text-xs uppercase tracking-[0.2em] text-cyan-200">
                <Sparkles size={14} /> SIH 2026 • Problem Statement 26139
              </motion.div>
              <h1 className="mt-6 text-5xl md:text-7xl font-black leading-[0.95] tracking-tight">
                Quantum Health AI
              </h1>
              <p className="mt-5 max-w-xl text-lg text-slate-300">
                Multimodal AI + Hybrid Quantum Machine Learning for Early Health-Risk Screening
              </p>
              <div className="mt-8 flex flex-wrap gap-4">
                <Link to="/screening" className="button-primary">Start Screening</Link>
                <Link to="/dashboard" className="button-secondary">Explore Platform</Link>
                <a href="#how-it-works" className="button-secondary">How It Works</a>
              </div>
            </div>

            <motion.div initial={{ opacity: 0, scale: 0.96 }} animate={{ opacity: 1, scale: 1 }} className="glass rounded-3xl p-6 relative overflow-hidden">
              <div className="grid-glow absolute inset-0 opacity-50" />
              <div className="relative space-y-3 text-sm text-cyan-100">
                {steps.map((step, index) => (
                  <div key={step} className="flex items-center gap-3">
                    <div className="flex flex-col items-center w-4">
                      <div className="h-2.5 w-2.5 rounded-full bg-cyan-400" />
                      {index < steps.length - 1 && <div className="h-8 w-px bg-cyan-500/40" />}
                    </div>
                    <span className="bg-slate-900/60 px-3 py-2 rounded-xl border border-cyan-400/20 w-full">{step}</span>
                  </div>
                ))}
              </div>
            </motion.div>
          </div>
        </section>

        <section id="problem" className="section-shell py-16">
          <div className="grid md:grid-cols-2 gap-8">
            <div className="glass rounded-3xl p-8">
              <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">Problem</p>
              <h2 className="mt-4 text-3xl font-bold">Early screening is fragmented and often lacks multimodal confidence.</h2>
            </div>
            <div className="glass rounded-3xl p-8 text-slate-300">
              Signs, voice, motion, and sensor data can be noisy or incomplete. Safe clinical decision support requires explainability, data quality checks, and reliability scoring rather than black-box diagnosis.
            </div>
          </div>
        </section>

        <section id="solution" className="section-shell py-8">
          <div className="grid md:grid-cols-3 gap-6">
            {[
              { icon: Activity, title: 'Multimodal AI', text: 'Fuse symptoms, voice, camera, and motion telemetry into one representation.' },
              { icon: BrainCircuit, title: 'Quantum ML', text: 'Explore classical, quantum, and hybrid QML pipelines on the same feature set.' },
              { icon: ShieldCheck, title: 'Safety-first', text: 'Risk assessment is presented as decision support, not a diagnosis.' },
            ].map(({ icon: Icon, title, text }) => (
              <div key={title} className="glass rounded-3xl p-6">
                <Icon className="text-cyan-300 mb-4" />
                <h3 className="text-xl font-semibold mb-2">{title}</h3>
                <p className="text-slate-300">{text}</p>
              </div>
            ))}
          </div>
        </section>

        <section id="how-it-works" className="section-shell py-20">
          <div className="text-center mb-10">
            <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">How It Works</p>
            <h2 className="text-4xl font-bold mt-4">From signals to screened insights</h2>
          </div>
          <div className="grid md:grid-cols-4 gap-5">
            {['Collect Signals','Quality Check','Model Analysis','Explainable Result'].map((item, index) => (
              <div key={item} className="glass rounded-2xl p-5">
                <div className="text-cyan-300 text-sm">0{index + 1}</div>
                <div className="mt-3 text-lg font-semibold">{item}</div>
              </div>
            ))}
          </div>
        </section>

        <section id="benchmarking" className="section-shell pb-20">
          <div className="glass rounded-3xl p-8">
            <div className="flex items-center justify-between gap-4 flex-wrap">
              <div>
                <p className="text-cyan-300 uppercase tracking-[0.2em] text-xs">Benchmark Center</p>
                <h2 className="text-3xl font-bold mt-3">QUANTUM ADVANTAGE REALITY CHECK</h2>
              </div>
              <Link to="/benchmark" className="button-primary inline-flex items-center gap-2">Open Benchmark <ArrowRight size={16} /></Link>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
