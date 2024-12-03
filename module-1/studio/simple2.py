# from types import TypedDict
# from langgraph.graph import StateGraph, START, END
# import random

# # State
# class State(TypedDict):
#     graph_state: str

# # Conditional edge
# def decide_mood(state) ->Literal['node_2', 'node_3']:
#     user_input = state['graph_state']

#     if random.random() < 0.5:
#         return 'node_2'

#     return 'node_3'

# # Nodes
# def node_1(state):
#     return {"graph_state": state['graph_state'] + " I am"}

# def node_2(state):
#     return {"graph_state": state['graph_state'] + " happy!"}

# def node_3(state):
#     return {"graph_state": state['graph_state'] + " sad!"}

# # Build graph
# builder = StateGraph(State)
# builder.add_node("node_1", node_1)
# builder.add_node("node_2", node_2)
# builder.add_node("node_3", node_3)
# builder.add_edge(START, "node_1")
# builder.add_conditional_edges("node_1", decide_mood)
# builder.add_edge("node_2", END)
# builder.add_edge("node_3", END)

# # Compile graph
# graph = builder.compile()

# graph.invoke({"graph_state": "Hi, this is Lance."})