import os

import requests
import streamlit as st

from frontend.components.chat_box import render_chat_box
from frontend.components.image_uploader import render_image_uploader
from frontend.components.incident_panel import render_incident_panel


API_URL = os.getenv("STREAMLIT_API_URL", "http://localhost:8000")


def call_agent(payload: dict) -> dict:
    """Call the FastAPI chat endpoint."""
    response = requests.post(f"{API_URL}/chat", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def upload_image(uploaded_file: object) -> str | None:
    """Upload image evidence to the backend."""
    if uploaded_file is None:
        return None
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
    response = requests.post(f"{API_URL}/upload/image", files=files, timeout=30)
    response.raise_for_status()
    return response.json()["saved_path"]


def call_incident_action(action: str, payload: dict) -> dict:
    """Call an incident action endpoint."""
    response = requests.post(f"{API_URL}/incidents/{action}", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def build_incident_payload(
    machine_id: str,
    error_code: str,
    user_message: str,
    agent_response: dict,
) -> dict:
    """Build a minimal incident payload from the current troubleshooting context."""
    return {
        "machine_id": machine_id,
        "error_code": error_code,
        "issue_summary": user_message or "Troubleshooting issue remains unresolved.",
        "ai_recommendation": agent_response.get("answer", "No agent recommendation was captured."),
    }


def main() -> None:
    st.set_page_config(page_title="PLC Troubleshooting Agent", layout="wide")
    st.title("PLC Troubleshooting Agent")

    with st.sidebar:
        st.header("Machine Context")
        machine_id = st.text_input("Machine ID", value="PLC-001")
        plc_type = st.text_input("PLC Type", value="Siemens S7-1200")
        error_code = st.text_input("Error Code", value="E-STOP")

    user_message = render_chat_box()
    uploaded_file = render_image_uploader()

    col_ask, col_unresolved, col_escalate = st.columns(3)
    agent_response: dict | None = st.session_state.get("agent_response")

    with col_ask:
        if st.button("Ask Agent", type="primary", use_container_width=True):
            image_path = upload_image(uploaded_file)
            payload = {
                "machine_id": machine_id,
                "plc_type": plc_type,
                "error_code": error_code,
                "message": user_message,
                "image_path": image_path,
            }
            with st.spinner("Asking agent..."):
                agent_response = call_agent(payload)
                st.session_state["agent_response"] = agent_response

    with col_unresolved:
        if st.button("Issue Not Resolved", use_container_width=True):
            if not agent_response:
                st.warning("Ask the agent before marking an issue unresolved.")
            else:
                payload = build_incident_payload(
                    machine_id=machine_id,
                    error_code=error_code,
                    user_message=user_message,
                    agent_response=agent_response,
                )
                result = call_incident_action("unresolved", payload)
                st.session_state["incident_action"] = result

    with col_escalate:
        if st.button("Escalate", use_container_width=True):
            if not agent_response:
                st.warning("Ask the agent before escalating an incident.")
            else:
                payload = build_incident_payload(
                    machine_id=machine_id,
                    error_code=error_code,
                    user_message=user_message,
                    agent_response=agent_response,
                )
                result = call_incident_action("escalate", payload)
                st.session_state["incident_action"] = result

    if agent_response:
        render_incident_panel(agent_response)

    incident_action: dict | None = st.session_state.get("incident_action")
    if incident_action:
        st.subheader("Incident Automation")
        st.write(f"Status: {incident_action.get('status', 'unknown')}")
        st.json(incident_action.get("automation", {}))


if __name__ == "__main__":
    main()
