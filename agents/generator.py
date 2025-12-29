def generator_agent(state):
    """
    Mock LLM generator to avoid external API calls.
    """
    question = state["question"]
    docs = state["documents"]

    context = " ".join([doc.page_content for doc in docs])

    if not context.strip():
        state["answer"] = "The document does not contain relevant information."
    else:
        state["answer"] = f"This document discusses the following content: {context[:300]}..."

    return state
