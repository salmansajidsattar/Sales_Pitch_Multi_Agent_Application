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




@tool("DuckDuckGoSearch")
def search(search_query: str):
    """Search the web for information on a given topic."""
    return DuckDuckGoSearchRun().run(search_query)

# Creating web scraping tool
scrape_tool = ScrapeWebsiteTool()
