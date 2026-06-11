from langchain_huggingface import HuggingFaceEmbeddings
import os
os.environ['HF_HOME'] = 'G:/huggingface_cache'

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

#single text
# text = 'Delhi is the capital of India.'

# multiple text
docs = [
    'Delhi is the capital of India.',
    'How are you?',
    'Good Morning Everyone!'
]
# for single line text
# vector = embedding.embed_query(text)

# for multiple texts
m_vector = embedding.embed_documents(docs)

print(str(m_vector))