from abc import ABC, abstractmethod


class BaseCleaner(ABC):

    @abstractmethod
    def clean(self, text: str) -> str:
        """Clears the text."""
        pass
