from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np



embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

docs = [
    'Delhi is the capital of India.',
    'How are you?',
    'Said every morning, Good Morning Everyone!'
]

query = 'What to said every morning?'

doc_embeddings = embedding.embed_documents(docs)
query_embedding = embedding.embed_query(query)

# print(cosine_similarity([query_embedding], doc_embeddings))

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index,score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(docs[index])
print('Similarity score is:', score)
