import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores.redis import Redis
from api_key import OPENAI_API_KEY
import redis
with st.sidebar:
    st.title('🤗💬 Chat with your Data')
    st.markdown('''
                ## About
    This app is an LLM-powered chatbot built using:
    - https://streamlit.io/
    - https://python.langchain.com/
    - https://platform.openai.com/docs/models LLM model
                ''')

def main():
    st.header("Chat with your own PDF")
    pdf = st.file_uploader("Upload your pdf", type="pdf")
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        texts = [page.extract_text() for page in pdf_reader.pages if page.extract_text() is not None]
        
        if texts:
            embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

            # Ensure you have a valid Redis URL
            VectorStore = Redis.from_texts(texts, embeddings, redis_url="redis://default:8s9g0Iq4RpGGquMycdIcFKNqQUuV6Nsk@redis-15557.c305.ap-south-1-1.ec2.cloud.redislabs.com:15557")
            # Connect to Redis server
            redis_client = redis.Redis(
            host='redis-15557.c305.ap-south-1-1.ec2.cloud.redislabs.com',
            port=15557,
            password='8s9g0Iq4RpGGquMycdIcFKNqQUuV6Nsk',
            db=0,
            decode_responses=True
)

            query = st.text_input("Ask questions related to your PDF")

            if query:
                results = VectorStore.similarity_search(query=query, k=3)
                llm = OpenAI(api_key=OPENAI_API_KEY)
                chain = load_qa_chain(llm=llm, chain_type="stuff")  # Adjust 'chain_type' as necessary
                response = chain.run(input_documents=results, question=query)
                st.write(response)
        else:
            st.write("No text could be extracted from the uploaded PDF. Please try another file.")
    else:
        st.write("Please upload a PDF file to proceed.")

if __name__ == '__main__':
    main()