import os
import sys
from pathlib import Path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ontology_service import OntologyService
from src.knowledge_graph_service import KnowledgeGraphService
from src.data_loader import DataLoader
from src.chat_handler import ChatHandler
from src.schema import OntologyConfig, KnowledgeGraphConfig, KGSources


def generate_ontology(sources: KGSources, ontology_config: OntologyConfig, recreate=False):
    
    data_loader = DataLoader()
    data = data_loader.load(sources)
    
    ontology = OntologyService()
    path = Path(ontology_config.path) / f"ontology-{ontology_config.name}.json"

    if os.path.exists(path) and os.path.isfile(path) and not recreate:
        print("ONTOLOGY EXISTED!")
        return ontology.load(path)
    
    return ontology.create(sources=data, config=ontology_config)


def generate_knowledge_graph(sources: KGSources, kg_config: KnowledgeGraphConfig):

    data_loader = DataLoader()
    data = data_loader.load(sources)
    
    ontology = OntologyService()
    ontology_path = Path(kg_config.ontology.path) / f"ontology-{kg_config.ontology.name}.json"
    if os.path.exists(ontology_path):
        print("ONTOLOGY EXISTED!")
        ontology = ontology.load(ontology_path)
    else:
        ontology.create(sources=data, config=kg_config.ontology)

    kg = KnowledgeGraphService(ontology=ontology, config=kg_config)
    return kg.create(data)


def extend_knowledge_graph(sources, kg_config):

    data_loader = DataLoader()
    data = data_loader.load(sources)
    
    ontology = OntologyService()
    ontology_path = Path(kg_config.ontology.path) / f"ontology-{kg_config.ontology.name}.json"
    if os.path.exists(ontology_path):
        print("ONTOLOGY EXISTED!")
        ontology = ontology.load(kg_config.ontology_path)
    else:
        ontology.create(sources=data, config=kg_config.ontology)

    kg = KnowledgeGraphService(ontology=ontology, config=kg_config)
    return kg.extend(data)

    
def chat(message, kb_name):
    chat_handler = ChatHandler()
    response = chat_handler.chat(message=message, graph_name=kb_name)
    return response
