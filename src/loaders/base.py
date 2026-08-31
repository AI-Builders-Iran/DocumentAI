from abc import abstractmethod, ABC
from pathlib import Path

from langchain_core.documents import Document


class BaseLoader(ABC):

    @abstractmethod
    def load(self, file: Path | str) -> list[Document]:
        """Load a document and return LangChain Documents."""
        pass
