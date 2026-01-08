import ollama

response = ollama.chat(
    model="llama3.1",
    messages=[
        {"role": "system", "content": "You are a precise technical assistant."},
        {"role": "user", "content": "In one paragraph, explain what an LLM is."}
    ],
    options={
        "temperature": 0.2
    }
)

print(response["message"]["content"])