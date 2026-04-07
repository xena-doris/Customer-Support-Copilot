from src.agent.agent import Agent

agent = Agent()

queries = [
    "How do I apply for benefits?",
    "My payment is not working and I have an issue"
]

for q in queries:
    print("\n====================")
    print("Query:", q)

    response = agent.handle_query(q)

    print("Tool Used:", response["tool_used"])
    print("Result:", response["result"])