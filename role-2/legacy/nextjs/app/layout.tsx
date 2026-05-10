import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "PLC Troubleshooting Agent",
  description: "Operator dashboard for PLC troubleshooting with RAG, SQL memory, vision, and n8n.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
