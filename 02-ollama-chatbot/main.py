import ollama

model_name="llama3.2:latest"

def ask_ollama(question):
    response=ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response["message"]["content"]