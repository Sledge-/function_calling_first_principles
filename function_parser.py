import json


external_functs = []

class FunctionParser:
    
    def __init__(self):
        self.history = []
        self.function_queue = {}
    
    def parse_output(self, text):
        # Append raw text to history
        self.history.append(text)
        
        # Check if the FUNCTION_CALL designator is in the text
        if "## FUNCTION_CALL ##" in text:
            # Extract the JSON portion
            json_start_index = text.index("## FUNCTION_CALL ##") + len("## FUNCTION_CALL ##")
            json_str = text[json_start_index:].strip()
            
            try:
                # Parse the JSON string
                parsed_json = json.loads(json_str)
                
                # Add to function queue with a default result of None
                self.function_queue[json_str] = None
                
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format detected.")
    
    def execute_function(self, function_str, external_funcs):
        # Parse the function string to extract the function name and parameters
        function_data = json.loads(function_str)
        func_name = function_data["name"]
        params = function_data["parameters"]  # Corrected this line
        
        # Check if the function exists in the provided external functions
        if func_name not in external_funcs:
            raise ValueError(f"No external function found for the name: {func_name}")
        
        # Execute the function
        result = external_funcs[func_name](**params)
        
        # Convert the result to string and store it in the function queue
        self.function_queue[function_str] = str(result)
    
    def retrieve_result(self, function_str):
        return self.function_queue.get(function_str, None)
    
    def clear_handled_function(self, function_str):
        if function_str in self.function_queue:
            del self.function_queue[function_str]

if __name__ == "__main__":
    # Sample output from the language model
    sample_output = """
    Here's a function call you requested:
    ## FUNCTION_CALL ##
    {
    "name": "sample_external_function",
    "parameters": {
    "group_by_columns": ["sale_date"],
    "value_columns": ["quantity", "total_price"],
    "aggregation_functions": ["sum", "sum"],
    "table_name": "food_truck_sales"
    }
    }
    """

    # Test the class with the corrected logic
    parser = FunctionParser()
    parser.parse_output(sample_output)
    parser.execute_function(list(parser.function_queue.keys())[0], {'sample_external_function': sample_external_function})
    result = parser.retrieve_result(list(parser.function_queue.keys())[0])

    result