import redis
from pathlib import Path
from typing import List
from fastapi import FastAPI, File, UploadFile
from src import services
from src.schema import OntologyConfig, KnowledgeGraphConfig, KGSources, ChatRequest


app = FastAPI()
redis_client = redis.StrictRedis(host="graph_db", port=6379, decode_responses=True)
sources_directory = Path("/sources")


@app.post('/chat')
def chat(chat_request: ChatRequest):
    response = services.chat(
        message=chat_request.message,
        kb_name=chat_request.graph_name
    )
    return {'response': response}


@app.post('/upload_files')
async def upload_files(files: List[UploadFile] = File(...)):
    sources_directory.mkdir(parents=True, exist_ok=True)

    uploaded_file_paths = []

    for file in files:
        file_path = sources_directory / file.filename
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        uploaded_file_paths.append(str(file_path))
    print(uploaded_file_paths)
    return uploaded_file_paths

@app.post('/create_ontology')
def create_ontology(
        sources: KGSources,
        config: OntologyConfig,
):
    try:
        response = services.generate_ontology(sources, config)
        return {'response': response}
    except Exception as e:
        print('ERROR MESSAGE:', e)


@app.post('/create_knowledgebase')
def create_knowledgebase(sources: KGSources, config: KnowledgeGraphConfig):
    response = services.generate_knowledge_graph(sources, config)
    return {'response': response}


@app.put('/extend_knowledgebase')
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
