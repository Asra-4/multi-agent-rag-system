from ingestion.loader import load_pdf
from ingestion.chunker import chunk_text
from vectorstore.store import create_vectorstore
from graph.rag_graph import build_graph

def main():
    text = load_pdf("sample_docs/sample.pdf")
    chunks = chunk_text(text)
    vectordb = create_vectorstore(chunks)

    graph = build_graph()

    while True:
        question = input("\nAsk a question (or exit): ")
        if question.lower() == "exit":
            break

        state = {"question": question, "vectordb": vectordb}
        answer = graph.invoke(state)
        print("\nAnswer:", answer)

if __name__ == "__main__":
    main()
