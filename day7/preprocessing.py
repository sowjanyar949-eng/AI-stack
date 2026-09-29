from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer("all-MiniLM-L6-v2")
with open("ai_sample.txt","r") as file:
    text = file.read()
#for line in text:
   # print(text)
#print("No of characters:",len(text))
chunks = []
chunks_size = 25
chunk_overlap = 10
step = chunks_size - chunk_overlap
for i in range(0,len(text),chunks_size):
    chunk = text[i:i+chunks_size]
    chunks.append(chunk)
#print("No of chunks:",len(chunks))
#for i in range(len(chunks)):
 #   print(f"chunk{i} -> {chunks[i]}")
 #Embeddings
embeddings= model.encode(chunks)
#print("Embeddings created successfully.")
#print("No of embeddings",len(embeddings))
#print(embeddings[0])
print(embeddings.shape)
#chroma db
client = chromadb.Client()

collection = client.create_collection(name="My_documents")
print("collection created successfully.")
#chroma db
client = chromadb.Client()
collection = client.create_collection(name="My_documents")
ids =[]
for i in range(len(chunk)):
    ids.append(str(i))
collection.add(
    ids=ids,
    documents=chunks
)
col=collection.get(ids=['0'])
print(col)