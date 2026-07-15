"""
Application configuration.
Loads environment variables and project constants.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --------------------------------------------------
# Base Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
CHROMA_DB_DIR = DATA_DIR / "chroma_db"

AUDIO_INPUT_DIR = BASE_DIR / "audio" / "input"
AUDIO_OUTPUT_DIR = BASE_DIR / "audio" / "output"

# Create directories automatically
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
CHROMA_DB_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_INPUT_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# API Keys
# --------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --------------------------------------------------
# Models
# --------------------------------------------------

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "llama-3.3-70b-versatile"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL",
    "base"
)

# --------------------------------------------------
# Text Splitter
# --------------------------------------------------

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# --------------------------------------------------
# Retriever
# --------------------------------------------------

TOP_K = 4