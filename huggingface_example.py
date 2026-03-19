import os
import requests

# API configuration
API_URL = "https://router.huggingface.co/hf-inference/models/gpt2"
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def query_huggingface(prompt):
    """Query Hugging Face API with a prompt"""
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt}
        )

        data = response.json()

        if isinstance(data, list):
            return data[0]["generated_text"]
        else:
            return data

    except Exception as e:
        return f"Error: {str(e)}"


# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Hugging Face API...")

    result = query_huggingface(user_prompt)

    print("Response:")
    print(result)