import os
from typing import Type

from google import genai
from pydantic import BaseModel

from src.schemas.common import GeneralDocument, DocumentType
from src.schemas.contract import Contract
from src.schemas.invoice import Invoice
from src.extraction.prompts import PromptBuilder

#------extract sructured information from document text using gemini-----------
class DocumentExtractor:

    _SCHEMA_MAP: dict[DocumentType, Type[BaseModel]] = {
        DocumentType.CONTRACT: Contract,
        DocumentType.INVOICE: Invoice,
        DocumentType.GENERAL: GeneralDocument,
    }

    def __init__(
        self,
        api_key: str | None = None,
        model_name: str = "gemini-2.5-flash",
    ) -> None:
        """
        initialize the document extractor.
         args:
            api_key: Gemini API key. if omitted, GEMINI_API_KEY is
                read from environment variables.
            model_name: Gemini model used for extraction.
        raises:
            valueError: if no API key is available.
        """
        self._api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self._api_key:
            raise ValueError("GEMINI_API_KEY is not set.")

        self._client = genai.Client(api_key=self._api_key)
        self._model_name = model_name
        self._prompt_builder = PromptBuilder()

    def extract(
        self,
        document_text: str,
        document_type: DocumentType,
    ) -> BaseModel:
        """
        extract structured information from document text.
        args:
            document_text: text extracted from the document.
            document_type: type of the document.
        returns:
            A validated pydantic model containing extracted information.
        raises:
            valueError: if the document type is not supported.
        """
        schema = self._get_schema(document_type)

        prompt = self._prompt_builder.build(
            document_text=document_text,
            document_type=document_type.value,
        )

        response = self._client.models.generate_content(
            model=self._model_name,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": schema,
            },
        )

        return schema.model_validate_json(response.text)

    def _get_schema(
        self,
        document_type: DocumentType,
    ) -> Type[BaseModel]:
        """
        return the pydantic schema associated with a document type.
        args:
            document_type: type of the document.
        returns:
            the corresponding pydantic model class.
        raises:
            valueError: if the document type is not supported.
        """
        try:
            return self._SCHEMA_MAP[document_type]
        except KeyError as exc:
            raise ValueError(
                f"Unsupported document type: {document_type}"
            ) from exc