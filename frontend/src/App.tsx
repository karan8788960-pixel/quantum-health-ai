import { Routes, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import DashboardShell from './components/DashboardShell';
import ScreeningPage from './pages/ScreeningPage';
import BenchmarkPage from './pages/BenchmarkPage';
import ReportsPage from './pages/ReportsPage';
import DemoModePage from './pages/DemoModePage';
import ResultsPage from './pages/ResultsPage';

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route element={<DashboardShell />}>
        <Route path="/dashboard" element={<div className="p-8 text-white">Dashboard overview</div>} />
        <Route path="/screening" element={<ScreeningPage />} />
        <Route path="/benchmark" element={<BenchmarkPage />} />
        <Route path="/reports" element={<ReportsPage />} />
        <Route path="/demo" element={<DemoModePage />} />
        <Route path="/result" element={<ResultsPage />} />
      </Route>
    </Routes>
  );
}
