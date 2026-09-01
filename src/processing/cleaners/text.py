import re

from .base import BaseCleaner


class TextCleaner(BaseCleaner):

    def clean(self, text: str) -> str:
        # Remove null characters
        text = text.replace("\x00", "")
        # Remove non-printable control characters
        text = re.sub(
            r"[\x01-\x08\x0B\x0C\x0E-\x1F\x7F]", "", text
        )
        # Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        return text
