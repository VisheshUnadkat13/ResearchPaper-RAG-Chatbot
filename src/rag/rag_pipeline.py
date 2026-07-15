"""
Complete RAG Pipeline.
"""

from src.rag.llm import LLM
from src.rag.prompts import RAG_PROMPT
from src.rag.retriever import Retriever


class RAGPipeline:

    def __init__(self, retriever):

        self.retriever = Retriever(retriever)

        self.llm = LLM.get_llm()

    def generate_answer(self, question: str) -> str:
        """
        Generate answer using RAG.
        """

        context = self.retriever.retrieve(question)

        prompt = RAG_PROMPT.invoke(
            {
                "context": context,
                "question": question
            }
        )

        response = self.llm.invoke(prompt)

        return response.content