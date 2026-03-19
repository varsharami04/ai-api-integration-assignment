import requests

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()
        return data.get("response", "No response returned")

    except Exception as e:
        return str(e)

prompt = input("Enter prompt: ")
print(query_ollama(prompt))