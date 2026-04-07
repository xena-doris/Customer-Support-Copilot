from .search_kb import SearchKB
from .create_ticket import CreateTicket


class ToolRegistry:
    def __init__(self):
        self.tools = {
            "SearchKB": SearchKB(),
            "CreateTicket": CreateTicket()
        }

    def get_tool(self, tool_name):
        return self.tools.get(tool_name)

    def list_tools(self):
        return list(self.tools.keys())