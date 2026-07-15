"""
Chroma Vector Database.

Responsible for:

1. Creating the vector database
2. Saving embeddings
3. Loading existing database
4. Creating retriever
"""

from langchain_chroma import Chroma
from langchain_core.documents import Document

from src.config import (
    CHROMA_DB_DIR,
    TOP_K
)
from src.rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.embedding_model = EmbeddingModel.get_embeddings()

    def create_vectorstore(
        self,
        chunks: list[Document]
    ) -> Chroma:
        """
        Create a new Chroma vector database.

        Args:
            chunks: Split documents.

        Returns:
            Chroma database instance.
        """

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=str(CHROMA_DB_DIR)
        )

        return vectorstore

    def load_vectorstore(self) -> Chroma:
        """
        Load an existing Chroma database.

        Returns:
            Chroma database instance.
        """

        vectorstore = Chroma(
            persist_directory=str(CHROMA_DB_DIR),
            embedding_function=self.embedding_model
        )

        return vectorstore

    @staticmethod
    def get_retriever(vectorstore: Chroma):
        """
        Convert vector database into retriever.

        Args:
            vectorstore: Chroma instance.

        Returns:
            Retriever
        """

        return vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": TOP_K
            }
        )