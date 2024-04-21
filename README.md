
**Chat with Your Data**

This project utilizes Streamlit, Langchain, and OpenAI to create an interactive chatbot that extracts text from uploaded PDF files and allows users to ask questions related to the content. 

**Key Features:**
- **PDF Upload:** Users can upload their own PDF files.
- **Text Extraction:** The app extracts text from the uploaded PDF using PyPDF2.
- **Embeddings:** Utilizes Langchain's OpenAIEmbeddings to generate embeddings for the extracted text.
- **Vector Storage:** Stores the embeddings in a Redis database using Langchain's Redis vector store.
- **Question Answering:** Uses Langchain's LLM (Large Language Model) to answer questions based on the uploaded text.
- **Streamlit Interface:** Provides a user-friendly interface for interacting with the chatbot.

**How to Use:**
1. **Upload PDF:** Choose a PDF file containing the text you want to analyze.
2. **Ask Questions:** Input questions related to the content of the PDF.
3. **View Answers:** The chatbot uses LLM to provide answers based on the uploaded text.

**Setup:**
- Ensure you have Python installed along with necessary libraries listed in the requirements.txt file.
- Obtain an OpenAI API key and update the `OPENAI_API_KEY` variable with your key.
- Adjust Redis connection details (`redis_url`, host, port, password) as per your setup.

**Deployment:**
- Clone this repository to your local machine.
- Install dependencies using `pip install -r requirements.txt`.
- Run the application with `streamlit run app.py`.
- Access the app through the provided URL.

**Contributing:**
Contributions are welcome! Feel free to open issues or pull requests for any enhancements or bug fixes.

**Credits:**
- Streamlit: [streamlit.io](https://streamlit.io/)
- Langchain: [python.langchain.com](https://python.langchain.com/)
- OpenAI: [platform.openai.com/docs/models](https://platform.openai.com/docs/models)

