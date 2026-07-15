"""
Embedding model configuration.

This module initializes the Hugging Face embedding model
used to convert text chunks into vector embeddings.
"""

from langchain_huggingface import HuggingFaceEmbeddings

from src.config import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Singleton class for HuggingFace Embeddings.
    """

    _embeddings = None

    @classmethod
    def get_embeddings(cls) -> HuggingFaceEmbeddings:
        """
        Returns a singleton embedding model.

        Returns:
            HuggingFaceEmbeddings
        """

        if cls._embeddings is None:

            cls._embeddings = HuggingFaceEmbeddings(
                model_name=EMBEDDING_MODEL,
                model_kwargs={
                    "device": "cpu"
                },
                encode_kwargs={
                    "normalize_embeddings": True
                }
            )

        return cls._embeddings