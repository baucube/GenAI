import warnings
warnings.filterwarnings("ignore")
from crewai import Agent, Task, Crew
# from crewai_tools import SerperDevTool, BaseTool
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

import os
# import pandas as pd
# from get_api_key import get_key



# Configuration des logs
os.environ["OPENAI_API_KEY"] = "NA"
# LLM Ollama
llm = ChatOllama(
    model="ollama/llama3:latest", 
    base_url="http://localhost:11434"
    )
# llm = ChatOpenAI(
#     model="ollama/phi3:3.8b",
#     base_url="http://localhost:11434/v1"
# )
# print(get_key()["my_groq_key"])

# llm_groq = ChatGroq(
#     temperature=0, 
#     groq_api_key=get_key()["my_groq_key"], 
#     model_name="ollama/llama-3.2-90b-vision-preview",
#     #model_name = "groq/llama-3.1-70b-versatile",
#     max_retries = 10,
#     )

# # Ajout d'un outil pour les recherches en ligne

# Agent
agent = Agent(
    role="Spécialiste en collecte de données touristiques",
    goal="Trouver et compiler une liste de 15 sites touristiques et centres d'intérêts du Sénégal",
    backstory="Tu es un expert en recherche touristique. Ta mission est d'identifier 15 sites et centres d'intérêts au Sénégal.",
    verbose=True,
    llm=llm
)

# Tâche
task = Task(
    description="Rechercher une liste de 15 sites touristiques au Sénégal avec noms et liens sources. Format JSON requis.",
    expected_output="Un objet json avec pour cle site_touristique",
    agent=agent
)

# Crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
)

# Exécution
result = crew.kickoff(inputs={"seach query":"Tous les sites touristiques du senegal"})
print(result)