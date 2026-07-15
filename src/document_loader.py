"""
Load research papers using LangChain.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class DocumentLoader:
    """
    Loads PDF documents using LangChain.
    """

    @staticmethod
    def load_pdf(pdf_path: str | Path) -> list[Document]:
        """
        Load a PDF and return LangChain Document objects.

        Args:
            pdf_path: Path to PDF file.

        Returns:
            List of LangChain Documents.
        """

        loader = PyPDFLoader(str(pdf_path))

        documents = loader.load()

        return documents