TOOLS = {
    "SearchKB": {
        "description": "Search knowledge base for relevant passages",
        "input": ["query"],
    },
    "GetPolicy": {
        "description": "Retrieve full section using section_id",
        "input": ["section_id"],
    },
    "CreateTicket": {
        "description": "Escalate issue by creating support ticket",
        "input": ["summary", "category", "severity"],
    },
    "AnswerDirect": {
        "description": "Answer without using tools",
        "input": ["response"],
    }
}