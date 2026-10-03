import { Outlet, Link } from 'react-router-dom';
import { Bell, Command, LayoutGrid, Search, UserCircle2 } from 'lucide-react';

const navItems = [
  'Dashboard', 'Patient Screening', 'Multimodal Assessment', 'Predictions', 'Classical ML', 'Quantum ML', 'Hybrid QML', 'Quantum Lab', 'Model Lab', 'Benchmark Center', 'Analytics', 'Dataset', 'Data Quality', 'Explainability', 'Robustness Lab', 'Fairness', 'Experiment History', 'Reports', 'Patient Registry', 'Appointments', 'Audit & Security', 'Settings', 'Help'
];

export default function DashboardShell() {
  return (
    <div className="min-h-screen bg-midnight text-slate-100">
      <div className="flex min-h-screen">
        <aside className="w-72 border-r border-slate-800 bg-slate-950/80 p-5 hidden xl:block">
          <div className="mb-8 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="h-10 w-10 rounded-xl bg-gradient-to-br from-cyan-300 to-violet-500 text-slate-900 font-bold flex items-center justify-center">Q</div>
              <div>
                <div className="font-bold">Quantum Health AI</div>
                <div className="text-xs text-slate-400">Research Console</div>
              </div>
            </div>
          </div>

          <div className="mb-6 rounded-2xl border border-cyan-500/25 bg-cyan-500/5 p-3">
            <div className="flex items-center gap-2 text-xs uppercase tracking-[0.18em] text-cyan-200"><Search size={14} /> Global Search</div>
            <div className="mt-3 flex items-center gap-2 rounded-full border border-slate-700 bg-slate-900/70 px-3 py-2 text-sm">
              <Command size={14} /> Ctrl+K / Cmd+K
            </div>
          </div>

          <div className="space-y-1 overflow-y-auto max-h-[calc(100vh-260px)] pr-1">
            {navItems.map((item) => (
              <Link key={item} to={item === 'Patient Screening' ? '/screening' : item === 'Benchmark Center' ? '/benchmark' : item === 'Reports' ? '/reports' : item === 'Patient Registry' ? '/dashboard' : '/dashboard'} className="block rounded-xl px-3 py-2 text-sm text-slate-300 hover:bg-slate-800/80 hover:text-white transition">
                {item}
              </Link>
            ))}
          </div>
        </aside>

        <div className="flex-1">
          <header className="border-b border-slate-800 bg-slate-950/70 backdrop-blur-md">
            <div className="flex items-center justify-between px-5 py-4">
              <div className="flex items-center gap-3 md:hidden">
                <LayoutGrid size={18} />
                <span className="font-semibold">Quantum Health AI</span>
              </div>
              <div className="hidden md:flex items-center gap-3 rounded-full border border-slate-700 bg-slate-900/70 px-3 py-2 text-sm text-slate-300">
                <Search size={14} /> Search commands...
              </div>
              <div className="flex items-center gap-4">
                <button className="relative rounded-full border border-slate-700 p-2 text-slate-200">
                  <Bell size={18} />
                  <span className="absolute -top-1 -right-1 h-2.5 w-2.5 rounded-full bg-cyan-400" />
                </button>
                <div className="flex items-center gap-3 rounded-full border border-slate-700 bg-slate-900/70 px-3 py-2">
                  <UserCircle2 size={22} className="text-cyan-300" />
                  <div>
                    <div className="text-sm font-medium">Dr. Aria Chen</div>
                    <div className="text-[10px] uppercase tracking-[0.18em] text-cyan-300">Doctor</div>
                  </div>
                </div>
              </div>
            </div>
          </header>

          <main className="p-5 md:p-8">
            <Outlet />
          </main>
        </div>
      </div>
    </div>
  );
}
