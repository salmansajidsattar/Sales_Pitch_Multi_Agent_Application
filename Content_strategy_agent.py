from crewai import Agent, Task
from helper import llm,scrape_tool,search

# Define the Content Strategy Agent
content_strategy_agent = Agent(
    role="Content Strategy Agent",
    goal="Develop content strategies and identify how improved content can drive engagement and conversions.",
    backstory=(
        "Specializes in creating a compelling narrative and strategy for content improvements on the client's website."
    ),
    allow_delegation=True,
    llm=llm,
    verbose=True
)

# Define the task for Content Strategy Agent
content_strategy_task = Task(
    description=(
        "Develop a content strategy for {company_name}'s website ({company_website}) to enhance user engagement and conversion rates."
    ),
    expected_output=(
        "Comprehensive content strategy for {company_name}'s website, including recommendations for content improvements."
    ),
    agent=content_strategy_agent,
    tools=[search, scrape_tool]
)