import re

from .base import BaseCleaner


class WhitespaceCleaner(BaseCleaner):

    def clean(self, text: str) -> str:
        """Removes extra spaces from text."""

        # Replace multiple spaces/tabs with a single space
        text = re.sub(
            r"[ \t]+", " ", text
        )

        # Replace 3 or more consecutive newlines with 2

        text = re.sub(
            r"\n{3,}", "\n\n", text
        )

        # Remove leading and trailing whitespace
        return text.strip()
