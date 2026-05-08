export function StatCard({ label, value }: { label: string; value: string }) {
  return (
    <article className="card">
      <div>{label}</div>
      <strong>{value}</strong>
    </article>
  );
}
