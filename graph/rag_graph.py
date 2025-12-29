from langgraph.graph import StateGraph, END
from agents.retriever import retriever_agent
from agents.generator import generator_agent
from agents.validator import validator_agent
from agents.final_response import final_response_agent

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("retriever", retriever_agent)
    graph.add_node("generator", generator_agent)
    graph.add_node("validator", validator_agent)
    graph.add_node("final", final_response_agent)

    graph.set_entry_point("retriever")
    graph.add_edge("retriever", "generator")
    graph.add_edge("generator", "validator")

    graph.add_conditional_edges(
        "validator",
        lambda state: "final" if state["valid"] else "generator",
        {"final": "final", "generator": "generator"}
    )

    graph.add_edge("final", END)

    return graph.compile()
