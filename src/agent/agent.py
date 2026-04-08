""" from src.tools.tool_registry import ToolRegistry
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
        } """

from src.tools.tool_registry import ToolRegistry
from src.policy.policy_model import ToolPolicyModel


class Agent:
    def __init__(self, kb):
        self.registry = ToolRegistry()
        self.policy = ToolPolicyModel()
        self.kb = kb   # 👈 IMPORTANT

    def handle_query(self, query):
        # 🧠 Step 1: Decide action using policy model
        decision = self.policy.decide(query)

        tool_name = decision.get("action")
        args = decision.get("arguments", {})

        tool = self.registry.get_tool(tool_name)

        if tool is None:
            return {"error": "Invalid tool"}

        # 🔧 Step 2: Execute tool
        if tool_name == "SearchKB":
            result = tool.run({
                "query": args.get("query", query),
                "kb": self.kb
            })

        elif tool_name == "CreateTicket":
            result = tool.run({
                "summary": args.get("summary", query),
                "category": args.get("category", "general"),
                "severity": args.get("severity", "medium")
            })

        elif tool_name == "AnswerDirect":
            result = {"response": args.get("response", "")}

        else:
            result = {"error": "Unknown action"}

        return {
            "decision": decision,
            "tool_used": tool_name,
            "result": result
        }