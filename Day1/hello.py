import ollama 
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Name only main types of AI"
        }
    ]
)
print(response['message']['content'])

