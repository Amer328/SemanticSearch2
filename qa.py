import os
import streamlit as st
import openai

# Fetch the OpenAI Key from Windows env
# api_key = os.environ["OPENAI_API_KEY"]
api_key = st.secrets["OPENAI_API"]

# Set the OpenAI key
openai.api_key = api_key


def create_prompt(context,query):
    header = "Answer the question as truthfully and with as much detail as possible using the provided context. Display the answer in bullet points. If the answer is not contained within the text and requires some information to be updated, print 'Sorry insufficient data to answer query' \n"
    return header + context + "\n\n" + query + "\n"


def generate_answer(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return(response.choices[0].message.content)
