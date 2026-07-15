import streamlit as st


def render_response_ui(answer: str):
    """Display chatbot response."""

    st.subheader("🤖 Answer")

    st.write(answer)

    st.button(
        "🔊 Listen to Answer",
        use_container_width=True
    )