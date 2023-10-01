
def load_text_file(file_path):
    """
    Load a text file and return its content.
    
    Parameters:
    - file_path (str): The path to the text file.
    
    Returns:
    - str: The content of the text file.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    return content


class PromptTemplate:
    def __init__(self, template):
        """
        A class to handle prompt templates and fill them with the provided values.

        The format of the template should be a normal string containing placeholders
        that are to be filled. Placeholders should be wrapped in double angle brackets
        in the format `<<placeholder_name>>`.

        For example:
        template_str = "Hello, my name is <<name>> and I am from <<city>>."

        Usage:
            prompt_template = PromptTemplate(template_str)
            filled_str = prompt_template.fill(name="John", city="New York")

        This will replace the placeholders with the provided values and return:
        "Hello, my name is John and I am from New York."

        Parameters:
        - template (str): The template string with placeholders.
        """
        self.template = template

    def fill(self, **kwargs):
        """
        Fill the template with the provided values.
        
        Parameters:
        - **kwargs: Keyword arguments representing placeholder names and their replacement values.
        
        Returns:
        - str: The filled template.
        """
        filled_template = self.template
        for key, value in kwargs.items():
            placeholder = f"<<{key}>>"
            filled_template = filled_template.replace(placeholder, value)
        return filled_template

    
if __name__ == "__main__":
    #: Testing the PromptTemplate class
    test_template_str = "Hello, my name is <<name>> and I am from <<city>>."
    test_prompt_template = PromptTemplate(test_template_str)
    test_filled_prompt = test_prompt_template.fill(name="John", city="New York")
    print(f"filled_prompt: {test_filled_prompt}")

    #: Test using linear_trend_request_prompt.txt
    linear_trend_prompt = load_text_file('linear_trend_request.prompt')
    linear_trend_prompt_template = PromptTemplate(linear_trend_prompt)
    # print(f"linear_trend_prompt_template.template: {linear_trend_prompt_template.template}")
    linear_trend_filled_prompt = linear_trend_prompt_template.fill(functions="<< add your function definitions here >>", 
    user_data="Here's a story involving some interesting commentary around trends in a market, supported by quantitative data.")
    print(f"linear_trend_filled_prompt: {linear_trend_filled_prompt}")