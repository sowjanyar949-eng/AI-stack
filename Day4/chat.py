import ollama
msgs =[
    {
        "role":"system",
        "content":"give the answers in single line only."
    }
]
while True:
    question = input("you:")
    if question.lower()=="exit":
        break
    msgs.append(
        {
            "role":"user",
            "content":question
        }
    )
    response=ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    msgs.append(
        {
            "role":"assistant",
            "content":response["message"]["content"]
        }
    )
    print("AI:",response["message"]["content"])
for msg in msgs:
    print(msg["role"]+":",msg["content"])
