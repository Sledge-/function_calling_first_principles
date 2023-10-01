import json

class FunctionParser:
    
    def __init__(self, external_funcs):
        self.external_funcs = external_funcs

    def parse_and_execute(self, text):
        """Parses the provided text and executes the function."""
        data = json.loads(text)

        # Extract the function data
        function_data = data.get("function_call")
        if not function_data:
            raise ValueError("No function call detected in the provided text.")
        
        func_name = function_data["name"]
        params = function_data["parameters"]

        # Check if the function exists in the provided external functions
        if func_name not in self.external_funcs:
            raise ValueError(f"No external function found for the name: {func_name}")

        # Execute the function
        return self.external_funcs[func_name](**params)

if __name__ == "__main__":
    from linear_trend_model import run_linear_trend_model

    # Sample output from the language model
    sample_output = """
{
    "function_call": {
        "name": "run_linear_trend_model", 
        "parameters": {
        "x": [20, 30, 50, 5],
        "y": [20, 15, 12, 35]
        }
    }
}
    """

    # Initialize the parser with the function
    parser = FunctionParser({'run_linear_trend_model': run_linear_trend_model})

    # Parse and execute
    result = parser.parse_and_execute(sample_output)
    print(result)
