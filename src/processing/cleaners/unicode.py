import unicodedata

from .base import BaseCleaner


class UnicodeCleaner(BaseCleaner):

    def clean(self, text: str) -> str:
        """Converts Unicode characters to a standard form."""

        return unicodedata.normalize("NFKC", text)
