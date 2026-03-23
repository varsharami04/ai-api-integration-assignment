# AI API Integration Project

#  Project Description

This project demonstrates how to integrate multiple Generative AI APIs using Python.  
It includes implementations for the following AI providers:

- Groq
- Ollama
- Hugging Face
- Cohere

Each program accepts user input, sends it to the respective API, and displays the AI-generated response.

#  Technologies Used

- Python
- APIs (Groq, Ollama, Hugging Face, Cohere)
- Requests Library
- Environment Variables

#  Setup Instructions

# 1. Clone the Repository

bash
git clone https://github.com/your-username/ai-api-integration.git
cd ai-api-integration

# 2. Create Virtual Environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

# 3. Install Dependencies
pip install -r requirements.txt

How to Get API Keys
Groq
Go to https://console.groq.com/
Sign up/login
Generate API key
export GROQ_API_KEY="your_key"

Hugging Face
Go to https://huggingface.co/
Create account
Generate token from settings
export HUGGINGFACE_API_KEY="your_token"

Cohere
Go to https://dashboard.cohere.com/
Create account
Generate API key
export COHERE_API_KEY="your_key"

Ollama
Download from https://ollama.ai/
Install and run:
ollama run llama3

How to Run Each Program
Groq
python groq_example.py

Ollama
python ollama_example.py

Hugging Face
python huggingface_example.py

Cohere
python cohere_example.py

# Screenshots

Groq Output
![Groq Output](screenshots/groq_output.png)

Ollama Output
![Ollama Output](screenshots/ollama_output.png)

Hugging Face Output
![Hugging Face Output](screenshots/huggingface_output.png)

Cohere Output
![Cohere Output](screenshots/cohere_output.png)
