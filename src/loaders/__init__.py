from .base import BaseLoader
from .document_loader import DocumentLoader
from .pdf_loader import PDFLoader
from .txt_loader import TXTLoader
from .docx_loader import DOCXLoader

__all__ = [
    "BaseLoader",
    "DocumentLoader",
    "PDFLoader",
    "TXTLoader",
    "DOCXLoader",
]