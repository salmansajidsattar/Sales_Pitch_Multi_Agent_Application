from crewai import Agent, Task
from helper import llm,scrape_tool,search


company_research_agent = Agent(
    role="Company Research Agent",
    goal="Gather detailed information about the target company, including their business, products, services, and market position.",
    backstory=(
        "Tasked with collecting comprehensive data about potential clients to inform the sales pitch."
    ),
    allow_delegation=True,
    llm=llm,
    verbose=True
)

# Define the task for Company Research Agent
company_research_task = Task(
    description=(
        "Collect comprehensive data about {company_name} from their website ({company_website}) and other sources. "
        "Include details about their business, products, services, and market position."
    ),
    expected_output=(
        "Detailed report on {company_name}'s business, products, services, and market position."
    ),
    agent=company_research_agent,
    tools=[search, scrape_tool]
)