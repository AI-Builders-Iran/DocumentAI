from langchain_core.documents import Document
from .cleaners.base import BaseCleaner
from langchain_core.documents import Document

from .cleaners.base import BaseCleaner


class DocumentProcessor:
    def __init__(self, cleaners: list[BaseCleaner]):
        self.cleaners = cleaners

    def process(self, documents: list[Document]) -> list[Document]:
        processed_docs = []

        for docs in documents:
            text = docs.page_content

            for cleaner in self.cleaners:
                text = cleaner.clean(text)

            processed_docs.append(
                Document(
                    page_content=text,
                    metadata=docs.metadata,
                )
            )
        return processed_docs
