import ollama 
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"System",
            "content":"Give answer in 2 lines only."
        }
    ]
)
print(response['message']['content'])