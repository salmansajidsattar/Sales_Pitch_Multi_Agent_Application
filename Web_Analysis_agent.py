from helper import llm,scrape_tool,search
from crewai import Agent, Task


# Define the Website Analysis Agent
website_analysis_agent = Agent(
    role="Website Analysis Agent",
    goal="Analyze the target company's website for areas of improvement, including design, performance, and user experience.",
    backstory=(
        "Focuses on identifying specific issues and opportunities for enhancement on the client's website."
    ),
    allow_delegation=True,
    llm=llm,
    verbose=True
)

# Define the task for Website Analysis Agent
website_analysis_task = Task(
    description=(
        "Analyze '''{company_name}'s website ({company_website}) to identify areas of improvement in design, performance, and user experience."
    ),
    expected_output=(
        "Detailed analysis report highlighting areas of improvement for {company_name}'s website, including design, performance, and user experience."
    ),
    agent=website_analysis_agent,
    tools=[scrape_tool, search]
)