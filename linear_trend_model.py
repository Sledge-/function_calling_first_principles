# Importing the linregress function from scipy's stats module.
# This function performs simple linear regression, a method used to describe a linear relationship between two variables.
from scipy.stats import linregress
import time

FUNCTIONS = [
    {
        "name": "run_linear_trend_model",
        "description": "This function runs a linear regression from two lists x,y which contain numeric data.",
        "properties": {
            "x": {
                "type": "array",
                "items": {
                    "type": "number"
                },
                "description": "List of numeric values representing the independent variable."
            },
            "y": {
                "type": "array",
                "items": {
                    "type": "number"
                },
                "description": "List of numeric values representing the dependent variable."
            }
        },
        "required": ["x", "y"],
    }
]

# Define the LinearTrendModel class.
class LinearTrendModel:
    '''
    Just a regular old linear regression model.
    '''
    def __init__(self, x, y):
        # x and y are the independent and dependent variables, respectively.
        self.x = x
        self.y = y
        print(f"x :{x}")
        print(f"y :{y}")

        # Initialize results to None. This attribute will store the output of the linear regression once the model is fitted.
        self.results = None
    
    # Method to fit a linear regression model.
    def fit(self):
        # Using the linregress function to perform linear regression on x and y.
        # The results (slope, intercept, etc.) are stored in the results attribute.
        t0 = time.time()
        self.results = linregress(self.x, self.y)
        print(f"fit linear model in {time.time() - t0} seconds.")
    
    # Method to retrieve the results of the linear regression.
    def get_results(self, return_str=False):
        if not self.results:
            raise ValueError("Model has not been fitted yet. Call the 'fit' method first.")
        
        # Construct the results dictionary
        results_dict = {
            "slope": self.results.slope,
            "intercept": self.results.intercept,
            "r_value": self.results.rvalue,
            "p_value": self.results.pvalue,
            "std_err": self.results.stderr
        }
        
        # Return either the string or dictionary representation based on the return_str flag
        if return_str:
            return str(results_dict)
        else:
            return results_dict
        
def run_linear_trend_model(x, y):
    """
    Wrapper function to run the LinearTrendModel class.
    
    Parameters:
    - x: List of numeric values representing the independent variable.
    - y: List of numeric values representing the dependent variable.
    
    Returns:
    - String representation of the linear regression results.
    """
    # Creating an instance of the LinearTrendModel class with the provided data.
    model = LinearTrendModel(x, y)
    
    # Fitting the linear regression model.
    model.fit()
    
    # Retrieving the string representation of the regression results.
    results_str = model.get_results(return_str=True)
    
    return results_str
    
if __name__ == "__main__":

    # Sample data for testing the class.
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Creating an instance of the LinearTrendModel class with the sample data.
    model = LinearTrendModel(x, y)
    # Fitting the linear regression model.
    model.fit()
    # Retrieving the results of the regression.
    results = model.get_results()
    results_str = model.get_results(return_str=True)
    results_dict = model.get_results(return_str=False)

    # Printing the results.
    print(f"results_str: {results_str}")
    print(f"results_dict: {results_dict}")

    # Test the wrapper function using the sample data
    x_sample = [1, 2, 3, 4, 5]
    y_sample = [2, 4, 6, 8, 10]
    output = run_linear_trend_model(x_sample, y_sample)
    output
