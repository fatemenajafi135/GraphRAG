from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    message: str
    graph_name: str


class KGSources(BaseModel):
    paths: List[str]


class OntologyConfig(BaseModel):

    name: str = "movies-6"
    path: str = "/home/fateme/graph_rag/knowledgebase/ontologies/"
    model_name: str = "gpt-4o-mini"
    ontology_prompt: str = """
        Extract only the most relevant information about all the movies, actors, and directors over the text.
        Avoid creating entities for details that can be expressed as attributes.
    """


class KnowledgeGraphConfig(BaseModel):

    name: str = 'movies-6'
    model_name: str = "gpt-4o-mini"
    ontology: OntologyConfig = OntologyConfig()
    cypher_system_instruction: str = ""
    qa_system_instruction: str = ""
    cypher_gen_prompt: str = ""
    cypher_gen_prompt_history: str = ""
    qa_prompt: str = ""



