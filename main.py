import streamlit as st
from io import StringIO
from vector_search import *
import qa
from utils import *


st.markdown("<h1 style='text-align: center; color: white;'>Semantic Search Engine for Documents and Q&A</h1>", unsafe_allow_html=True)



st.title("Example Questions")
st.text("In what way might migration influence the quality of parent-child relationships in refugee families?")
st.text("What are the mental health challenges refugees face during the settlement process in the host country?")
st.text("What are typical family relationship challenges and speculate on their impact on the mental health problems of refugee adolescents?")
st.text("What demographic variables may influence mental health problems in refugee adolescents?")
st.text("How can mental health professionals and other stakeholders work together to improve the process of mental health care?")
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
            # commented out
            
            st.success("Database Updated")
    if 'Ask a question' in options:
        with st.spinner("Searching for the answer..."):
            source,res = find_match(query,3)
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

            
            


       
