from pathlib import Path

from langchain_core.documents import Document

from .base import BaseLoader
from .docx_loader import DOCXLoader
from .pdf_loader import PDFLoader
from .txt_loader import TXTLoader


class DocumentLoader:
    _loaders: dict[str, type[BaseLoader]] = {
        ".pdf": PDFLoader,
        ".docx": DOCXLoader,
        ".txt": TXTLoader
    }

    @classmethod
    def load(cls, file: Path | str) -> list[Document]:
        file = Path(file)
        extension = file.suffix.lower()
        loader_class = cls._loaders.get(extension)

        if loader_class is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )
        loader = loader_class()
        return loader.load(file)


