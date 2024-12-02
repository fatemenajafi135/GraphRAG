from langchain.chains.graph_qa.falkordb import FalkorDBQAChain
from langchain_community.graphs import FalkorDBGraph
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


class ChatHandler:

    def chat(self, message, graph_name):

        graph = FalkorDBGraph(database=graph_name, port=6379, host='graph_db')
        chain = FalkorDBQAChain.from_llm(
            ChatOpenAI(temperature=0),
            graph=graph,
            verbose=False,
            allow_dangerous_requests=True
        )
        response = chain.run(message)
        return response
