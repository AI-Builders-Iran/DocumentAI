from enum import Enum
from pydantic import BaseModel

class DocumentType(str, Enum):
    CONTRACT = "contract"
    INVOICE = "invoice"
    GENERAL = "general"

class GeneralDocument(BaseModel):
    document_type: DocumentType = DocumentType.GENERAL