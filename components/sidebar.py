import streamlit as st


def render_sidebar():
    """Render the application sidebar."""

    with st.sidebar:

        st.title("📄 Research Paper Chatbot")

        st.markdown("---")

        st.subheader("🛠 Tech Stack")

        st.markdown("""
- 🐍 Python
- 🦜 LangChain
- 🧠 Groq LLM
- 🤗 Hugging Face Embeddings
- 🗂️ ChromaDB
- 🎤 Speech-to-Text
- 🔊 Text-to-Speech
- 🌐 Streamlit
""")

        st.markdown("---")

        st.subheader("📌 Instructions")

        st.markdown("""
1. Upload a research paper.
2. Wait until indexing is complete.
3. Ask questions using text or speech.
4. Read or listen to the answer.
""")

        st.markdown("---")

        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.answer = ""
            st.success("Chat history cleared.")