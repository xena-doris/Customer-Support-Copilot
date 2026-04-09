from src.tools.tool_registry import ToolRegistry
from src.policy.policy_model import ToolPolicyModel
from src.generator.generator_model import GeneratorModel   # 👈 NEW


class Agent:
    def __init__(self, kb):
        self.registry = ToolRegistry()
        self.policy = ToolPolicyModel()
        self.generator = GeneratorModel()   # 👈 NEW
        self.kb = kb

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
            # 🧠 Clean query from policy model
            clean_query = args.get("query", query)

            # 🔥 Fix: prevent garbage query from model
            if not clean_query or len(clean_query) > 100 or "action" in clean_query.lower():
                clean_query = query

            tool_output = tool.run({
                "query": clean_query,
                "kb": self.kb
            })

            passages = tool_output.get("results", [])

            # 🧠 Step 3: Generate final answer using LLM
            generated_answer = self.generator.generate(query, passages)

            result = {
                "raw_passages": passages,
                "generated_answer": generated_answer
            }

        elif tool_name == "CreateTicket":
            result = tool.run({
                "summary": args.get("summary", query),
                "category": args.get("category", "general"),
                "severity": args.get("severity", "medium")
            })

        elif tool_name == "AnswerDirect":
            result = {
                "generated_answer": args.get("response", "")
            }

        else:
            result = {"error": "Unknown action"}

        return {
            "decision": decision,
            "tool_used": tool_name,
            "result": result
        }