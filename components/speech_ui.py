import streamlit as st


def render_speech_ui():
    """Render speech input placeholder."""

    st.subheader("🎤 Speech Input")

    st.info(
        "Speech recording will be integrated using Whisper "
        "in the next phase."
    )

    if st.button(
        "🎙 Start Recording",
        use_container_width=True
    ):

        st.warning("Speech recording is not implemented yet.")

    return None