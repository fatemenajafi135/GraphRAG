# GraphRAG
An implementation of GraphRAG using graphrag-sdk, falkordb, langchain, ...

## Project Overview
This project is a robust service for managing, generating, and interacting with Knowledge Graphs (KG) using the **GraphRAG-SDK**, **FalkorDB**, and **LangChain**. The service provides a flexible and scalable platform for handling different file types, creating ontologies, generating KGs, extending them, and interacting with them via chat.

Key features of this project include:
- **GraphRAG-SDK**: Used for managing the creation and processing of Knowledge Graphs.
- **FalkorDB**: Stores and evolves the generated KGs in a highly efficient and scalable manner.
- **LangChain**: Powers the conversational chat interface, enabling interactions with the knowledge stored in the KG.
- **FastAPI**: The service is built as a FastAPI application to provide a fast and efficient API layer for interacting with the system.
- **Dockerized with Docker Compose**: The entire service is containerized for easy deployment, with CI/CD pipelines via GitHub Actions for continuous integration and delivery.

## Features
- **Ontology Creation**: Define and create an ontology to structure the data for the KG.
- **Knowledge Graph Generation**: Generate a KG based on a provided ontology and various data sources (PDF, Word, PowerPoint).
- **KG Extension**: Add new data and extend the existing KG.
- **Chat Interface**: Interact with the generated KG via a conversational chat powered by LangChain.
- **File Upload**: Upload files for future processing and integration.
  
## How to Run the Service

### Prerequisites
- Python 3.11
- Docker and Docker Compose installed
- FastAPI and other Python dependencies

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/fatemenajafi135/GraphRAG.git
   cd GraphRAG
    ```

2. Build and run the Docker containers: The project uses Docker Compose to set up the necessary services.
    ```shell
    docker-compose up --build
    ```
   This will:

- Build the FastAPI service container.
- Set up the FalkorDB container for storing the Knowledge Graph.
- Ensure that the CI/CD pipeline for GitHub Actions is ready for automatic deployment.

3. Access the FastAPI documentation: Once the services are running, you can access the FastAPI documentation at:
    ```shell
    http://localhost:8000/docs
    ```

4. CI/CD Pipeline (GitHub Actions): The repository is integrated with GitHub Actions for CI/CD automation. It automatically builds, tests, and deploys containers upon any changes to the codebase. All relevant configuration files for GitHub Actions can be found in the `.github/workflows/` directory.

5. Available APIs
The service exposes the following APIs for interacting with the Knowledge Graph:

- POST /ontology/create: Create a new ontology based on a provided sources.
- POST /kg/create: Generate a new Knowledge Graph based on the defined ontology.
- PUT /kg/extend: Extend an existing Knowledge Graph by adding new data.
- POST /kg/upload-files: upload files for future processing and integration. (URL, PDF, Word, PowerPoint).
- POST /chat: Chat interface to interact with the Knowledge Graph via LangChain.

## Technologies Used AND WHY

- **GraphRAG-SDK**: 
  - Framework for generating and managing Knowledge Graphs.
  - Chosen for its ability to efficiently manage the process of generating and processing complex Knowledge Graphs.
- **FalkorDB**: 
  - A scalable, production-grade graph database to store the Knowledge Graph.
  - Ideal for storing graph-based data, providing fast querying and scalability.
- **LangChain**: 
  - Conversational AI chain for querying and interacting with the Knowledge Graph.
  - A powerful tool for building conversational AI chains, perfect for creating chat interfaces with knowledge graphs.
- **FastAPI**: 
  - A modern web framework for creating APIs.
  - Known for its high performance and easy integration with modern Python-based APIs.
- **Docker & Docker Compose**: 
  - Containerization and orchestration for the entire service.
  - Ensures consistency in deployment across environments and simplifies managing dependencies.
- **GitHub Actions**: 
  - CI/CD for automated testing and deployment.
