import json

def extract_json_from_text(text):
    """Revised function to extract a JSON string embedded within a text."""
    
    # Find the start index of "function_call" keyword
    keyword_index = text.find("function_call")
    if keyword_index == -1:
        raise ValueError("Keyword 'function_call' not found in the text.")
    
    # Find the start of the entire JSON string (the opening curly bracket before "function_call")
    start_index = text.rfind("{", 0, keyword_index)
    if start_index == -1:
        raise ValueError("Opening curly bracket not found before 'function_call'.")
    
    # Track curly brackets to find the end of the JSON string
    counter = 0
    end_index = -1
    for i in range(start_index, len(text)):
        if text[i] == "{":
            counter += 1
        elif text[i] == "}":
            counter -= 1
            if counter == 0:  # Found the end of the JSON string
                end_index = i
                break
    
    if end_index == -1:
        raise ValueError("Matching closing curly bracket not found.")
    
    # Extract the JSON string
    json_str = text[start_index:end_index + 1]
    return json_str


class FunctionParser:
    def __init__(self, external_funcs):
        self.external_funcs = external_funcs

    def parse_and_execute(self, text):
        """Parses the provided text and executes the function."""
        # Extract the JSON string from the text using the revised helper function
        json_str = extract_json_from_text(text)
        
        # Parse the JSON
        data = json.loads(json_str)

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
    def dummy_function(x, y):
        return sum(x), sum(y)

    #: Example 1
    # Sample output from the language model
    sample_output = """
{
    "function_call": {
        "name": "dummy_function", 
        "parameters": {
        "x": [20, 30, 50, 5],
        "y": [20, 15, 12, 35]
        }
    }
}
"""
    print(f"sample_output: {sample_output}")

    # Initialize the parser with the function
    parser = FunctionParser({'dummy_function': dummy_function})

    # Parse and execute
    result = parser.parse_and_execute(sample_output)
    print(result)


    #: Example 2
    # Sample output from the language model with leading text.
    sample_output = """
Here is the function call to run a linear regression on the data provided:

{
  "function_call": {
    "name": "dummy_function",
    "parameters": {
      "x": [0.5, 1.5, 3, 4.2, 6], 
      "y": [15000, 12500, 10000, 7500, 6000]
    }
  }
}
"""
    print(f"sample_output: {sample_output}")

    # Initialize the parser with the function
    parser = FunctionParser({'dummy_function': dummy_function})

    # Parse and execute
    result = parser.parse_and_execute(sample_output)
    print(result)


        #: Example 3
    # Another example with different format.
    sample_output = """
Here is more dummy data with a new format.

Will the parser be able to do to it?

{
  "function_call": {
    "name": "dummy_function2",
    "parameters": {
      "id": "Karl",
      "date": "11/20/1999",
      "location": "Earth"
    }
  }
}
"""
    print(f"sample_output: {sample_output}")
    def dummy_function2(id, date, location):
        print(f"{id}, {date}, {location}")
        return True

    # Initialize the parser with the function
    parser = FunctionParser({'dummy_function2': dummy_function2})

    # Parse and execute
    result = parser.parse_and_execute(sample_output)
    print(result)
