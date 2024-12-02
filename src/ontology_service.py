import os
import json
from pathlib import Path
from graphrag_sdk import Ontology
from graphrag_sdk.models.openai import OpenAiGenerativeModel
from schema import OntologyConfig


openai_api_key = os.getenv("OPENAI_API_KEY")


class OntologyService:

    def __init__(self):
        self.ontology = None

    def create(self, sources, config: OntologyConfig):
        model = OpenAiGenerativeModel(model_name=config.model_name)
        self.ontology = Ontology.from_sources(
            sources=sources,
            boundaries=config.ontology_prompt,
            model=model,
        )
        self._save_ontology(config.name, config.path)
        return self.ontology

    # def create_manually(self):
    #     pass

    def _save_ontology(self, name, base_path):
        os.makedirs(base_path, exist_ok=True)
        path = Path(base_path) / f"ontology-{name}.json"
        with open(path, "w", encoding="utf-8") as file:
            file.write(json.dumps(self.ontology.to_json(), indent=2))
        print('Ontology saved here: ', path)

    def load(self, path):
        with open(path, "r", encoding="utf-8") as file:
            representation = json.load(file)
        self.ontology = Ontology.from_json(representation)
        return self.ontology
