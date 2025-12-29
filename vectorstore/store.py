from langchain_community.vectorstores import Chroma
from langchain_core.embeddings import Embeddings

class MockEmbeddings(Embeddings):
    """
    Mock embeddings to avoid external API calls.
    """

    def embed_documents(self, texts):
        return [[0.01] * 768 for _ in texts]

    def embed_query(self, text):
        return [0.01] * 768

def create_vectorstore(chunks):
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=MockEmbeddings(),
        persist_directory="chroma_db"
    )
    
    return vectordb
