"""
Split research paper into smaller chunks.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from src.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class TextSplitter:
    """
    Split LangChain documents into chunks.
    """

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Split documents into chunks.

        Args:
            documents: LangChain documents.

        Returns:
            List of chunked documents.
        """

        return self.splitter.split_documents(documents)