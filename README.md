```
ResearchPaper-RAG-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
├── .gitignore
│
├── data/
│   ├── uploads/
│   └── chroma_db/
│
├── audio/
│   ├── input/
│   └── output/
│
├── assets/
│   ├── logo.png
│   └── styles.css
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── utils.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── document_loader.py
│   │   ├── text_splitter.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── llm.py
│   │   ├── prompts.py
│   │   └── rag_pipeline.py
│   │
│   └── speech/
│       ├── __init__.py
│       ├── recorder.py
│       ├── speech_to_text.py
│       └── text_to_speech.py
│
├── components/
│   ├── __init__.py
│   ├── sidebar.py
│   ├── upload_section.py
│   ├── chat_ui.py
│   ├── speech_ui.py
│   └── response_ui.py
│
└── tests/
```
