from src.tools.tool_registry import ToolRegistry
from .tool_router import ToolRouter


class Agent:
    def __init__(self):
        self.registry = ToolRegistry()
        self.router = ToolRouter()

    def handle_query(self, query):
        tool_name = self.router.route(query)

        tool = self.registry.get_tool(tool_name)

        if tool_name == "SearchKB":
            result = tool.run({"query": query})

        elif tool_name == "CreateTicket":
            result = tool.run({
                "summary": query,
                "category": "general",
                "severity": "medium"
            })

        else:
            result = {"error": "No tool found"}

        return {
            "tool_used": tool_name,
            "result": result
        }