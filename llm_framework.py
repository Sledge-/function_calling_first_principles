import json
from function_parser import FunctionParser

class LLMFramework:
    def __init__(self, bedrock_runtime, prompt, functions):
        self.bedrock_runtime = bedrock_runtime
        self.prompt = prompt
        self.functions = functions
        self.function_parser = FunctionParser(self.functions)
        self.conversation_history = ""
    
    def communicate_with_llm(self, filled_prompt):
        body = json.dumps({"prompt": filled_prompt, "max_tokens_to_sample": 500})
        modelId = "anthropic.claude-v2"
        accept = "application/json"
        contentType = "application/json"

        print(f"body: {body}")
        response = self.bedrock_runtime.invoke_model(
            body=body, modelId=modelId, accept=accept, contentType=contentType
        )
        response_body = json.loads(response.get("body").read())
        completion = response_body.get("completion")
        print(f"completion: {completion}")
        return completion
    
    def run(self):
        iterations = 0
        max_iterations = 20  # or any number you deem appropriate

        while iterations < max_iterations:
            print(f"iterations: {iterations}")
            # Create the prompt including the conversation history
            filled_prompt = self.prompt + self.conversation_history
            completion = self.communicate_with_llm(filled_prompt)
            
            # Execute function and get result
            try:
                result = self.function_parser.parse_and_execute(completion)
                print(f"result: {result}")
            except ValueError as e:
                print(f"An error occurred: {e}")
                return result

            # Add the LLM response and the function results to the conversation history
            self.conversation_history += "\n\nAssistant:\n" + completion + "\n\nResult:\n" + str(result) + "\n\nAssistant:\n"

            # Assess the result (for now, I'm just checking if it's a positive trend)
            if result[1] > result[0]:
                return result

            iterations += 1

        return "Failed to find a positive trend after max iterations."
    

if __name__ == "__main__":
    from linear_trend_model import run_linear_trend_model, FUNCTIONS
    from prompt_template import PromptTemplate, load_text_file
    import os
    from utils import bedrock

    #: Here's our prompt that we'll use to drive the language model
    linear_trend_agent_prompt = load_text_file('linear_trend_model_agent.prompt')

    #: Here's some mock sales KPI data generated for our hypothetical hot dog stand.
    city_dogs_stats =  load_text_file('city_dogs_stats.txt')

    #: Establish the Prompt template from the text file.
    linear_trend_agent_prompt_template = PromptTemplate(linear_trend_agent_prompt)

    #: Fill the prompt using our agent prompt and FUNCTIONS
    linear_trend_agent_filled_prompt = linear_trend_agent_prompt_template.fill(
        FUNCTIONS=str(FUNCTIONS), #: JSON schema definition of the functions
        user_data=city_dogs_stats
    )
    print(f"linear_trend_agent_filled_prompt: {linear_trend_agent_filled_prompt}")

    #: Get the bedrock runtime
    bedrock_runtime = bedrock.get_bedrock_client(
        assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
        region=os.environ.get("AWS_DEFAULT_REGION", None)
    )

    #: Need to give the actual python function to the LLM as well
    functions  = {"run_linear_trend_model": run_linear_trend_model}

    #: Initialize our framework
    llm_framework = LLMFramework(bedrock_runtime, linear_trend_agent_filled_prompt, functions)

    #: Run it
    result = llm_framework.run()

    print(f"RESULT: {result}")


