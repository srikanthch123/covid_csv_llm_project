# from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Ask any question from your CSV")
st.header("Ask any question from your yploaded CSV file")


csv_file = st.file_uploader("Upload CSV file", type="csv")


def csv_file_function(csv_file):
    if csv_file is not None:
        agent = create_csv_agent(
            OpenAI(temperature=0.5), csv_file, verbose=True)
        return agent
    

user_question = st.text_input("Ask a question about your CSV: ")
response=csv_file_function(csv_file)
if user_question is not None and user_question != "":
    with st.spinner(text="In progress..."):
        st.write(response.run(user_question))
    
    

   



