import { StatCard } from "../../components/stat-card";

export default function DashboardPage() {
  return (
    <section>
      <h1>Dashboard</h1>
      <div className="grid">
        <StatCard label="Open incidents" value="0" />
        <StatCard label="High-priority incidents" value="0" />
        <StatCard label="Average confidence" value="0.00" />
        <StatCard label="Average latency" value="0 ms" />
        <StatCard label="Notification success" value="0%" />
      </div>
    </section>
  );
}
