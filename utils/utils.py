def extract_model_info(data):
    """
    Extracts modelName and modelId pairs from the provided data.
    
    Parameters:
    - data (dict): The input data format.
    
    Returns:
    - list of tuples: Ordered tuple of modelName, modelId pairs.
    """
    # Extract model summaries from the data
    model_summaries = data.get("modelSummaries", [])
    
    # Extract modelName and modelId pairs
    model_info = [(entry["modelName"], entry["modelId"]) for entry in model_summaries]
    
    return model_info


# Sample data for testing
sample_data = {
    'modelSummaries': [
        {
            'modelId': 'amazon.titan-tg1-large',
            'modelName': 'Titan Text Large'
        },
        {
            'modelId': 'amazon.titan-e1t-medium',
            'modelName': 'Titan Text Embeddings'
        },
        # ... additional entries can be added here
    ]
}

if __name__ == "__main__":
    # Test the function
    extracted_info = extract_model_info(sample_data)
    print(f"extracted_info: {extracted_info}")