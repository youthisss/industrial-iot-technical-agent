export default function IncidentDetailPage({ params }: { params: { id: string } }) {
  return (
    <section>
      <h1>Incident {params.id}</h1>
      <div className="card">
        Incident summary, AI recommendation, sources, confidence, notifications, and maintenance
        history placeholder.
      </div>
    </section>
  );
}
