from typing import Dict, TypedDict, Optional, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate


load_dotenv()

groq_key = os.getenv('GROQ_KEY')


llm = ChatGroq(api_key = groq_key,
                 temperature = 0,
                 model = "llama-3.2-90b-vision-preview")



class State(TypedDict):
    question: str = 'Olá'


def chatbot(state: State):
    question = state['question']
    
    print(llm.invoke(question).content)


graph_builder = StateGraph(State)


graph_builder.add_edge(START, 'chatbot')

graph_builder.add_node('chatbot',chatbot)

graph_builder.add_edge('chatbot',END)

graph = graph_builder.compile()



if __name__ == '__main__':

    #graph.get_graph().draw_mermaid_png(output_file_path='graph.png')

    while True:
        try:
            questao = input('Faça uma pergunta: ')
            state = {'question': questao}
            graph.invoke(state)

        except:
            print('finalizando')
            break