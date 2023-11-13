import os
import streamlit as st
import openai

# Fetch the OpenAI Key from Windows env
# api_key = os.environ["OPENAI_API_KEY"]
# api_key = st.secrets["OPENAI_API"]
# api_base = st.secrets["OPENAI_API_BASE"]

# Set the OpenAI key


from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2023-05-15"
)


def create_prompt(context,query):
    header = "Answer the question with as much detail as possible using the provided context and support your answer with paragraphs and bullet points. If no answer is generated, print 'Sorry insufficient data to answer query' \n"
    return header + context + "\n\n" + query + "\n"


def generate_answer(prompt):

    response = client.chat.completions.create(
    model="DAAGPT416k",
    #model ="DAAGPT35turbo16k",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.1,
    max_tokens=13000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return(response.choices[0].message.content)

