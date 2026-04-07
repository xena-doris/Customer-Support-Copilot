class BaseTool:
    name = ""
    description = ""
    input_schema = {}
    output_schema = {}

    def run(self, input_data):
        raise NotImplementedError