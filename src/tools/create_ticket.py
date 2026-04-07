from .base_tool import BaseTool
import uuid


class CreateTicket(BaseTool):
    name = "CreateTicket"

    description = "Create a support ticket for unresolved issues."

    input_schema = {
        "summary": "string",
        "category": "string",
        "severity": "low/medium/high"
    }

    output_schema = {
        "ticket_id": "string"
    }

    def run(self, input_data):
        ticket_id = "TCK" + str(uuid.uuid4())[:8]

        # Simulate storage (later you can connect DB)
        print("\n🎫 Ticket Created:")
        print(input_data)

        return {
            "ticket_id": ticket_id
        }