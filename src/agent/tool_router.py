class ToolRouter:
    def route(self, query):
        query = query.lower()

        if "issue" in query or "problem" in query or "not working" in query:
            return "CreateTicket"

        return "SearchKB"