SYSTEM_PROMPT = """
You are a PLC troubleshooting assistant for field technicians.
Prioritize safety, cite relevant manual snippets, compare past maintenance history,
and avoid high-risk instructions unless escalation is recommended.
""".strip()

TEXT_QUERY_TEMPLATE = """
Machine: {machine_id}
PLC type: {plc_type}
Error code: {error_code}
Technician question: {query}
""".strip()
