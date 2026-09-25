import ollama 
while True:
    question =input("ask me question:")
    if question.lower()=="exit":
        break
        
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role":"user",
                "content":"Name only main types of AI"
            },
            {
                "role":"user",
                "content":question
            }
        ]
    )
    print(response['message']['content'])

