from langchain_cohere import ChatCohere
from langchain_cohere import CohereEmbeddings
import streamlit as st


llm = ChatCohere(
    cohere_api_key = st.secrets["COHERE_API_KEY"],
)

embeddings = CohereEmbeddings(model="embed-english-light-v3.0")
