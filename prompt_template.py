class PromptTemplate:
    def __init__(self, template):
        """
        Initialize the PromptTemplate with a template string.
        
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
        return self.template.format(**kwargs)
    
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
    
if __name__ == "__main__":
    #: Testing the PromptTemplate class
    template_str = "Hello, my name is {name} and I am from {city}."
    prompt_template = PromptTemplate(template_str)
    filled_prompt = prompt_template.fill(name="John", city="New York")
    print(f"filled_prompt: {filled_prompt}")

    #: Test using linear_trend_request_prompt.txt
    linear_trend_prompt = load_text_file('linear_trend_request_prompt.txt')
    linear_trend_prompt_template = PromptTemplate(linear_trend_prompt)
    # print(f"linear_trend_prompt_template.template: {linear_trend_prompt_template.template}")
    linear_trend_filled_prompt = linear_trend_prompt_template.fill(functions="<< add your function definitions here >>", 
    user_data="Here's a story involving some interesting commentary around trends in a market, supported by quantitative data.")
    print(f"linear_trend_filled_prompt: {linear_trend_filled_prompt}")