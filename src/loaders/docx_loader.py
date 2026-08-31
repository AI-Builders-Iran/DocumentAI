from pathlib import Path

from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.documents import Document

from .base import BaseLoader


class DOCXLoader(BaseLoader):

    def load(self, file: Path | str) -> list[Document]:
        """Loads a DOCX from langchain"""
        loader = Docx2txtLoader(
            file_path=str(file)
        )
        return loader.load()
