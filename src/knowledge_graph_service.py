from falkordb import FalkorDB
from graphrag_sdk import KnowledgeGraph
from graphrag_sdk.model_config import KnowledgeGraphModelConfig
from graphrag_sdk.models.openai import OpenAiGenerativeModel
from src.schema import KnowledgeGraphConfig


class KnowledgeGraphService:

    def __init__(self, ontology, config: KnowledgeGraphConfig):
        self.ontology = ontology
        self.config = config
        self.kb = None

    def create(self, sources):
        if self.kb is None:
            model = OpenAiGenerativeModel(model_name=self.config.model_name)
            self.kg = KnowledgeGraph(
                name=self.config.name,
                model_config=KnowledgeGraphModelConfig.with_model(model),
                ontology=self.ontology,
                # cypher_system_instruction=self.config.cypher_system_instruction,
                # qa_system_instruction=self.config.qa_system_instruction,
                # cypher_gen_prompt=self.config.cypher_gen_prompt,
                # cypher_gen_prompt_history=self.config.cypher_gen_prompt_history,
                # qa_prompt=self.config.qa_prompt
            )
            self.kg.process_sources(sources)
        return f"KG named {self.config.name} created!"

    def create_manually(self, sources):
        pass

    def extend(self, sources):
        if self.kb is None:
            self.select_kg()
        self.kg.process_sources(sources)

    def select_kg(self):
        db = FalkorDB()
        if self.kb is None:
            self.kb = db.select_graph(self.config.name)
        return "Graph-BD loaded!"