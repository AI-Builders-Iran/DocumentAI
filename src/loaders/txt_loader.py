from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from .base import BaseLoader


class TXTLoader(BaseLoader):

    def load(self, file: Path | str) -> list[Document]:
        """Loads a TXT from langchain"""
        loader = TextLoader(file_path=str(file))
        return loader.load()
