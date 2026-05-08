import streamlit as st


def render_chat_box() -> str:
    """Render the technician question input."""
    return st.text_area(
        "Troubleshooting Question",
        value="What should I check after an emergency stop reset?",
        height=140,
    )
