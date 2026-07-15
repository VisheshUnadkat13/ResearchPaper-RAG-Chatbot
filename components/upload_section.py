import streamlit as st


def render_upload_section():
    """Render the PDF upload section."""

    uploaded_file = st.file_uploader(
        "📄 Upload Research Paper",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success(f"✅ Uploaded: {uploaded_file.name}")

        if st.button(
            "📥 Process Research Paper",
            use_container_width=True
        ):

            with st.spinner("Processing research paper..."):

                # RAG pipeline will be added later.

                st.session_state.paper_uploaded = True

            st.success("Research paper indexed successfully!")