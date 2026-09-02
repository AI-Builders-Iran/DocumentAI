from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseChunker(ABC):

    @abstractmethod
    def chunk(self, document: Document) -> list:
        pass
