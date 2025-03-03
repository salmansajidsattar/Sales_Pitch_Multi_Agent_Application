from dotenv import load_dotenv
load_dotenv()
import os
from crewai_tools import ScrapeWebsiteTool
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from crewai import LLM

llm = LLM(
    model="ollama/llama3",
    base_url="http://localhost:11434"
)

# llm = LLM(
#     api_key="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",
#     model="groq/llama-3.2-3b-preview",
#     temperature=0.7,
#     max_tokens=100
# )
# llm = LLM(
#     api_key="AIzaSyAwY0gznMaycu4RMaj5PT1IjudRgzJEFlY",
#     model="gemini/gemini-1.5-pro",
#     temperature=0.4
# )




@tool("DuckDuckGoSearch")
def search(search_query: str):
    """Search the web for information on a given topic."""
    return DuckDuckGoSearchRun().run(search_query)

# Creating web scraping tool
scrape_tool = ScrapeWebsiteTool()
