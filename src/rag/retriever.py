"""
Retriever helper.
"""

from langchain_core.documents import Document


class Retriever:

    def __init__(self, retriever):
        self.retriever = retriever

    def retrieve(self, question: str) -> str:
        """
        Retrieve relevant chunks and return as text.
        """

        documents: list[Document] = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        return context