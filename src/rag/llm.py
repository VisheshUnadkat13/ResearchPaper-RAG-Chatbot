"""
Groq LLM configuration.
"""

from langchain_groq import ChatGroq

from src.config import (
    GROQ_API_KEY,
    LLM_MODEL,
)


class LLM:

    _llm = None

    @classmethod
    def get_llm(cls):
        """
        Returns singleton Groq LLM.
        """

        if cls._llm is None:

            cls._llm = ChatGroq(
                groq_api_key=GROQ_API_KEY,
                model_name=LLM_MODEL,
                temperature=0
            )

        return cls._llm