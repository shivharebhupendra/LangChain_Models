# LangChain Models

A hands-on repository for learning and experimenting with LangChain, Large Language Models (LLMs), Chat Models, and Embedding Models.

## Project Structure

```text
LangChain_Models/
│
├── 1.LLMs/
│   └── llm_demo.py
│
├── 2.ChatModels/
│   ├── chatmodels_google.py
│   ├── chatmodel_huggingface_api.py
│   └── chatmodelshuggingface_local.py
│
├── 3.EmbeddedModels/
│   ├── embedding_hf_local.py
│   └── document_similarity.py
│
├── requirements.txt
└── test.py
```

## Topics Covered

### 1. LLMs

* Introduction to Large Language Models
* LangChain LLM Integration
* Text Generation

### 2. Chat Models

* Google Gemini Integration
* Hugging Face API Models
* Local Hugging Face Models
* Conversational AI Applications

### 3. Embedding Models

* Text Embeddings
* Sentence Transformers
* Semantic Similarity
* Document Comparison

## Installation

Clone the repository:

```bash
git clone https://github.com/shivharebhupendra/LangChain_Models.git
cd LangChain_Models
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add your API keys:

```env
GOOGLE_API_KEY=your_api_key
HUGGINGFACEHUB_API_TOKEN=your_api_token
```

## Learning Goals

* Understand LangChain fundamentals
* Work with different LLM providers
* Learn Chat Models and Prompt Engineering
* Explore Embeddings and Vector Representations
* Build AI-powered applications

## Technologies Used

* Python
* LangChain
* Hugging Face
* Google Gemini
* Sentence Transformers

## Author

Bhupendra Shivhare

Learning AI, Machine Learning, Generative AI, and LangChain through practical projects.
