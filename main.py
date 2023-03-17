import streamlit as st
from io import StringIO
from vector_search import *
import qa
from utils import *

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>Semantic Search Engine for Audit Documents and Q&A</h1>", unsafe_allow_html=True)

st.title("Example Questions")
st.text("Explain the importance of financial controls")
st.text("What ethical requirements are auditors are subject to ?")
st.text("What are the Auditor's Responsibilities for the Audit of the Financial Statements?")
st.text("What factors can lead to a Decision to Investigate by the case examiner from the FRC?")
st.text("In the preparation of financial statements, how do you decide materiality ?")
st.text("")

filename = False
query = False
options = st.radio(
    'Choose task',
    ('Ask a question','Update the Database of Documents'))

if 'Update the Database' in options:
    filename = st.text_input("Enter the full path of the PDF document")
    
if 'Ask a question' in options:
    query = st.text_input("Enter your question")

button = st.button("Submit")
  
if button and (filename or query):
    if 'Update the Database' in options:
        with st.spinner("Updating Database..."):
            corpusData = scrape_text_from_pdf(filename)
            addData(corpusData,filename)
            st.success("Database Updated")
    if 'Ask a question' in options:
        with st.spinner("Searching for the answer..."):
            source,res = find_match(query,2)
            # Arrange the matching result as source, data, source ,data etc
            result = []
            for i in range(len(source)):
                result.append(source[i])
                result.append(res[i])

            context= "\n\n".join(result)
            st.expander("Context").write(context)
            prompt = qa.create_prompt(context,query)
            answer = qa.generate_answer(prompt)
            # answer = str(source[0]) + "\n" + answer
            st.success("Answer: "+answer)

            
            


       