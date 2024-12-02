from graphrag_sdk.source import URL, PDF, TEXT
from langchain_community.document_loaders import Docx2txtLoader, UnstructuredPowerPointLoader
from src.utils import save_txt


class DataLoader:
    
    def load(self, sources):
        return [self._load_source(source) for source in sources.paths]
    
    def _load_source(self, source_path):

        print('Loading... ', source_path)
        if source_path.endswith(".pdf"):
            return self._load_pdf(source_path)
        elif source_path.endswith(".docx"):
            return self._load_docx(source_path)
        elif source_path.endswith(".pptx"):
            return self._load_pptx(source_path)
        elif source_path.startswith("http"):
            return self._load_url(source_path)
        else:
            return ''
            # raise ValueError(f"Unsupported source type: {source}")

    @staticmethod
    def _load_pdf(source_path):
        return PDF(source_path)

    @staticmethod
    def _load_docx(source_path):
        loader = Docx2txtLoader(source_path)
        data = loader.load()
        new_path = save_txt(source_path=source_path, data=data)
        return TEXT(new_path)
        # return Document(content=data[0].page_content)

    @staticmethod
    def _load_pptx(source_path):
        loader = UnstructuredPowerPointLoader(source_path)
        data = loader.load()
        new_path = save_txt(source_path=source_path, data=data)
        return TEXT(new_path)

    @staticmethod
    def _load_url(source_path):
        print(type(URL(source_path)))
        return URL(source_path)
