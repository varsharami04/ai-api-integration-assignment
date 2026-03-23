# huggingface_example.py

import requests
import os

# Configure API
api_key = os.getenv("HUGGINGFACE_API_KEY")
API_URL ="https://router.huggingface.co/hf-inference/models/bigscience/bloom-560m"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Dummy client to match assignment structure
class HuggingFaceClient:
    def __init__(self, headers, url):
        self.headers = headers
        self.url = url

    def generate(self, prompt, max_tokens=500, temperature=0.7):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={"inputs": prompt}
        )

        data = response.json()

        class Result:
            def __init__(self, text):
                self.text = text

        if isinstance(data, list):
            return Result(data[0]["generated_text"])
        else:
            return Result(str(data))

# Initialize client
client = HuggingFaceClient(headers, API_URL)

def query_api(prompt):
    """Query the Hugging Face API with a prompt"""
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt}
        )

        # DEBUG INFO
        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)

        # Handle empty response
        if not response.text.strip():
            return "Error: Empty response from API"

        # Try JSON parsing
        try:
            data = response.json()
        except:
            return f"Error: Non-JSON response → {response.text}"

        if isinstance(data, list):
            return data[0].get("generated_text", "No text generated")
        else:
            return data

    except Exception as e:
        return f"Error: {str(e)}"
# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")

    result = query_api(user_prompt)

    print("Response:")
    print(result)
print("API KEY:", api_key)