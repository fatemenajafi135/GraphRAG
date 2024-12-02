import os
from langchain.chains.graph_qa.falkordb import FalkorDBQAChain
from langchain_community.graphs import FalkorDBGraph
from langchain_openai import ChatOpenAI


openai_api_key = os.getenv("OPENAI_API_KEY")


class ChatHandler:

    def chat(self, message, graph_name):

        graph = FalkorDBGraph(database=graph_name, port=6379, host='graph_db')
        chain = FalkorDBQAChain.from_llm(
            ChatOpenAI(
                openai_api_key=openai_api_key,
                temperature=0
            ),
            graph=graph,
            verbose=False,
            allow_dangerous_requests=True,
            openai_api_key=openai_api_key
        )
        response = chain.run(message)
        return response
