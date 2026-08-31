from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from .base import BaseLoader


class PDFLoader(BaseLoader):

    def load(self, file: Path | str) -> list[Document]:
        """load pdf from langchain"""
        loader = PyPDFLoader(
            file_path=str(file)
        )
        return loader.load()
