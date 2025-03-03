from crewai import Crew,Process
from Web_Analysis_agent import website_analysis_agent,website_analysis_task
from sales_pitch_agent import sales_pitch_agent,sales_pitch_task
from Research_agent import company_research_agent,company_research_task
from Content_strategy_agent import content_strategy_agent,content_strategy_task
import streamlit as st
import time


# Instantiate the Crew
def Create_Crew()->Crew:
    return Crew(
        agents=[
            company_research_agent,
            website_analysis_agent,
            content_strategy_agent,
            sales_pitch_agent
        ],
        tasks=[
            company_research_task,
            website_analysis_task,
            content_strategy_task,
            sales_pitch_task
        ],
        # verbose=True,
        # memory=True,
        # cache=True,
        process=Process.sequential
    )
crew=Create_Crew()
# Title of the app
st.title("Company Information Form")

# Input fields for company name and website link
company_name = st.text_input("Enter Company Name")
website_link = st.text_input("Enter Company Website Link")
inputs = {
    "company_name": company_name,
    "company_website": website_link
}

# Submit button
if st.button("Submit"):
    # Check if both fields are filled
    if company_name and website_link:
        # Display a loader while processing
        with st.spinner("Processing your request..."):
            # Simulate a delay (e.g., API call or processing)
            result = crew.kickoff(inputs= inputs)
            time.sleep(3)  # Replace this with your actual processing logic
            # Display the response in markdown format
            st.markdown(result)
    else:
        st.warning("Please fill in both fields before submitting.")