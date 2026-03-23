# cohere_example.py

import cohere
import os

# Configure API
api_key = os.getenv("COHERE_API_KEY")
client = cohere.Client(api_key)

def query_api(prompt):
    """Query the Cohere API with a prompt"""
    try:
        response = client.chat(
            model="command-r-08-2024",
            message=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Cohere API...")

    result = query_api(user_prompt)

    print("Response:")
    print(result)