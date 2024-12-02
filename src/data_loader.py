from graphrag_sdk.source import URL


class DataLoader:
    
    def load(self, sources):
        return [self._load_source(source) for source in sources.paths]
    
    def _load_source(self, source):
        if source.endswith(".pdf"):
            return self._load_pdf(source)
        elif source.endswith(".docx"):
            return self._load_docx(source)
        elif source.startswith("http"):
            print('url', source)
            return self._load_url(source)
        else:
            raise ValueError(f"Unsupported source type: {source}")
    
    def _load_pdf(self, source):
        # Logic to load PDF
        pass
        
    def _load_docx(self, source):
        # Logic to load DOCX
        pass
    
    def _load_url(self, source):
        return URL(source)

