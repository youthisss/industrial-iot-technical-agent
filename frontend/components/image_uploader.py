import streamlit as st


def render_image_uploader() -> object | None:
    """Render image uploader for panel photos or HMI screenshots."""
    return st.file_uploader(
        "Upload PLC panel or HMI image",
        type=["png", "jpg", "jpeg"],
    )
