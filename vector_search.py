import pinecone
from sentence_transformers import SentenceTransformer,util
import streamlit as st

model = SentenceTransformer('all-MiniLM-L6-v2') #384 dimensional

pinecone_api_key = st.secrets["PINECONE_API"]

pinecone.init(api_key=pinecone_api_key, environment="gcp-starter") 
index = pinecone.Index("ai-assist1")

def rebuildIndex:
    pinecone.delete_index(index)
    pinecone.create_index(index, dimension=384,metric='cosine', replicas=1, pod_type='s1.x1')


def addData(corpusData,url):
    id  = index.describe_index_stats()['total_vector_count']
    for i in range(len(corpusData)):
        chunk=corpusData[i]
        chunkInfo=(str(id+i),
                model.encode(chunk).tolist(),
                {'title': url,'context': chunk})
        index.upsert(vectors=[chunkInfo])


def find_match(query,k):
    query_em = model.encode(query).tolist()
    result = index.query(query_em, top_k=k, includeMetadata=True)
    
    return [result['matches'][i]['metadata']['title'] for i in range(k)],[result['matches'][i]['metadata']['context'] for i in range(k)]
   
