import redis
from fastapi import FastAPI
from src import services
from src.schema import OntologyConfig, KnowledgeGraphConfig, KGSources, ChatRequest


app = FastAPI()
redis_client = redis.StrictRedis(host="graph_db", port=6379, decode_responses=True)

@app.post('/chat')
def chat(chat_request: ChatRequest):
    response = services.chat(
        message=chat_request.message,
        kb_name=chat_request.graph_name
    )
    return {'response': response}


@app.post('/create_ontology')
def create_ontology(sources: KGSources, config: OntologyConfig):
    response = services.generate_ontology(sources, config)
    return {'response': response}


@app.post('/create_knowledgebase')
def create_knowledgebase(sources: KGSources, config: KnowledgeGraphConfig):
    response = services.generate_knowledge_graph(sources, config)
    return {'response': response}


@app.post('/extend_knowledgebase')
def extend_knowledgebase(sources: KGSources, config: KnowledgeGraphConfig):
    response = services.extend_knowledge_graph(sources, config)
    return {'response': response}


@app.get('/check_db_connection')
def db_connection_check():
    try:
        redis_client.ping()
        return {"message": "Connected to FalkorDB!"}
    except redis.ConnectionError:
        return {"error": "Failed to connect to FalkorDB"}


@app.get('/')
def root():
    return {"response": 'GraphRAG service!'}
