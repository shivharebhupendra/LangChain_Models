# import langchain

# print(langchain.__version__)

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "meta-llama/Llama-3.1-8B-Instruct"
)

print("Model access successful!")