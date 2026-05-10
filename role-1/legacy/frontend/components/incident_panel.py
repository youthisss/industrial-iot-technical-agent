import streamlit as st


def render_incident_panel(response: dict) -> None:
    """Render the agent response and retrieved evidence."""
    st.subheader("Agent Response")
    st.write(response.get("answer", "No response."))
    st.caption(f"Safety level: {response.get('safety_level', 'unknown')}")

    sources = response.get("retrieved_sources", [])
    if sources:
        st.subheader("Retrieved Sources")
        for source in sources:
            with st.expander(source.get("source", "Unknown source")):
                st.write(source.get("content", ""))
                st.caption(f"Score: {source.get('score', 0)}")

    history = response.get("maintenance_history", [])
    if history:
        st.subheader("Maintenance History")
        st.dataframe(history, use_container_width=True)
