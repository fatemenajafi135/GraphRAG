# GraphRAG
An implementation of GraphRAG using graphrag-sdk, falkordb, langchain, ...


## Running Manually

- DB:
```shell
docker pull falkordb/falkordb:edge
docker run -p 6379:6379 -p 3000:3000 -it --rm -v ./knowledgebase:/knowledgebase falkordb/falkordb:edge
```

- FASTAPI
```shell
fastapi run app.py
```
 