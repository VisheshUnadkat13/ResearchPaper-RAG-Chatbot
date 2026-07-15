import streamlit as st

from components.sidebar import render_sidebar
from components.upload_section import render_upload_section
from components.chat_ui import render_chat_ui
from components.speech_ui import render_speech_ui
from components.response_ui import render_response_ui


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Research Paper RAG Chatbot",
    page_icon="📄",
    layout="wide"
)


# -------------------------------------------------
# Session State
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "paper_uploaded" not in st.session_state:
    st.session_state.paper_uploaded = False

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "transcribed_text" not in st.session_state:
    st.session_state.transcribed_text = ""


# -------------------------------------------------
# Sidebar
# -------------------------------------------------

render_sidebar()


# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("📄 Research Paper RAG Chatbot")

st.markdown(
    """
Ask questions about any research paper using **RAG + Groq + ChromaDB + LangChain**.

Upload a research paper to get started.
"""
)


# -------------------------------------------------
# Upload Section
# -------------------------------------------------

render_upload_section()


# -------------------------------------------------
# Chat Section
# -------------------------------------------------

if st.session_state.paper_uploaded:

    st.divider()

    question = render_chat_ui()

    st.divider()

    speech_question = render_speech_ui()

    final_question = question if question else speech_question

    if final_question:
        # RAG Pipeline will be called here later

        answer = "RAG response will appear here."

        st.session_state.answer = answer

        render_response_ui(answer)

else:
    st.info("👆 Please upload a research paper first.")