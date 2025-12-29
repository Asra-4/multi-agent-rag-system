def retriever_agent(state):
    query = state["question"]
    vectordb = state["vectordb"]

    # Retrieving top 3 most relevant chunks
    docs = vectordb.similarity_search(query, k=3)

    # Storing retrieved documents in state
    state["documents"] = docs

    return state
