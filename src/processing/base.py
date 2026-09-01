from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseProcessor(ABC):

    @abstractmethod
    def process(self, documnet: Document) -> Document:
        """
        Process a single document.
        """
        pass
