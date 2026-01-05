from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver
from agents.coordinator_agent import coordinator_agent

memory = MemorySaver()
graph = StateGraph()

graph.add_node("travel", coordinator_agent)
graph.set_entry_point("travel")

travel_graph = graph.compile(checkpointer=memory)
