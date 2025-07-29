import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

OPENAI_API_KEY = "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"
st.header("Notebot")

with st.sidebar:
    st.title = "My notes"
    file = st.file_uploader("Upload notes pdf and start asking questions", type = "pdf")

if file is not None:
    my_pdf = PdfReader(file)
    text=""
    for page in my_pdf.pages:
        text += page.extract_text()
        #st.write(text)

    #break it into chuncks
    splitter=RecursiveCharacterTextSplitter(separators=["\n"], chunk_size=50, chunk_overlap=50)
    chunks = splitter.split_text(text)
    #st.write(chunks)

    #helps in connecting to OpenAI embedding models through OpenAPI key
    embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

    #Generates embeddings, creating vectorDB and storing embeddings into it
    vector_store=FAISS.from_texts(chunks,embeddings)

    #get user query
    user_query = st.text_input = ("Type your query here")

    #sematic search from vector store
    if user_query:
        matching_chunks = vector_store.similarity_search(user_query)

    #define our LLM
    llm = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        max_tokens=300,
        temperature=0,
        model="gpt-3.5-turbo"
    )

    #Generate response
    load_qa_chain(llm,chain_type="stuff")
    output = chain.run(question=user_query, input_documents=matching_chunks)
    st.write(output)