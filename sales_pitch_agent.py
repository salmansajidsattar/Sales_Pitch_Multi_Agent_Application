from crewai import Agent, Task
from helper import llm,scrape_tool,search

# Define the Sales Pitch Agent
sales_pitch_agent = Agent(
    role="Sales Pitch Agent",
    goal="Create a personalized and persuasive sales pitch to convince the target company to have their website modified by 'Code With Salman'.",
    backstory=(
        "Combines research, analysis, and content strategy to craft a compelling sales pitch."
    ),
    allow_delegation=False,
    llm=llm,
    verbose=True
)

# Define the task for Sales Pitch Agent
sales_pitch_task = Task(
    description=(
        "Combine the research, analysis, and content strategy to create a personalized and persuasive sales pitch for {company_name} "
        "to convince them to have their website modified by 'Code With Salman'."
    ),
    expected_output=(
        "Customized sales pitch for {company_name}, highlighting the benefits of having their website modified by 'Code With Salman'."
    ),
    agent=sales_pitch_agent,
    tools=[search, scrape_tool]
)