import streamlit as st


def render_chat_ui():
    """Render text question input."""

    st.subheader("💬 Ask a Question")

    question = st.text_input(
        "Type your question",
        placeholder="Example: What is the methodology used in this paper?"
    )

    ask = st.button(
        "🚀 Ask",
        use_container_width=True
    )

    if ask and question.strip():
        return question

    return None