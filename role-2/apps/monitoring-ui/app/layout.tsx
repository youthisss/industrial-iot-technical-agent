import "./globals.css";

export const metadata = {
  title: "PLC Monitoring UI",
  description: "Monitoring UI for PLC troubleshooting incidents",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <nav>
          <a href="/dashboard">Dashboard</a>
          <a href="/incidents">Incidents</a>
          <a href="/machines">Machines</a>
          <a href="/telemetry">Telemetry</a>
          <a href="/agent-runs">Agent Runs</a>
        </nav>
        <main>{children}</main>
      </body>
    </html>
  );
}
