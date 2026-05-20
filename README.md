# Multi-Agent RAG System


## Overview

This project implements a Retrieval-Augmented Generation (RAG) system that enables users to ask questions about document content. The system ingests documents, extracts and processes text, stores embeddings in a vector database, and answers user queries using an agentic workflow orchestrated with LangGraph.

The focus of this implementation is on **system architecture, agent orchestration, and retrieval flow**, rather than reliance on external APIs.

---

## High-Level Architecture

1. **Document Ingestion**
   - Supports PDF documents
   - OCR interface designed to integrate with DeepSeek OCR
   - OCR is mocked for demonstration and offline execution

2. **Text Processing**
   - Text cleaning and normalization
   - Semantic chunking using `RecursiveCharacterTextSplitter`

3. **Embeddings & Vector Store**
   - ChromaDB is used as the vector database
   - Embeddings are automatically persisted to disk
   - Relevant document chunks are retrieved during question answering

4. **Agentic RAG Workflow (LangGraph)**
   - Retriever Agent: Fetches relevant document chunks
   - Generator Agent: Produces an answer using retrieved context
   - Validator Agent: Demonstrates conditional control flow and retry logic
   - Final Response Agent: Returns the validated response

---

## Vector Store & Embeddings

ChromaDB is used as the vector store with persisted embeddings.  
Due to API quota constraints, embeddings are mocked using LangChain’s `Embeddings` interface, while preserving the full retrieval architecture. The design allows seamless replacement with real embedding models.

During question answering, relevant document chunks are retrieved from the vector store and passed to the generator agent.

---

## Validation Agent

A validator agent is implemented to demonstrate **conditional control flow and retry logic** using LangGraph.

For demonstration purposes with mocked LLM responses, the validator accepts the first generated response to prevent infinite retries. The design supports stricter validation rules (e.g., hallucination detection, relevance scoring) when real LLMs are enabled.

---

## LLM Generation

The generator agent is implemented with a mock LLM to demonstrate agentic control flow and RAG architecture without external API dependency.

Integration points for OpenAI or Gemini models are clearly defined and can be enabled by providing valid API credentials via environment variables.

---

## Technology Stack

- Python
- LangChain
- LangGraph
- ChromaDB
- dotenv
- Streamlit (optional UI)

---


## Setup Instructions

### 1. Create Environment

```bash
conda create -n annervia python=3.10
conda activate annervia
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

### Create a .env file using the example provided:

```bash
OPENAI_API_KEY=your_api_key_here
```

### Running the Application (CLI)

```bash
python app.py
```

## You will be prompted to enter a question related to the document.

## Sample Interaction

## User: What is this document about?
## Assistant: This document discusses the following content: diabetes mellitus. It references multiple studies including Diabetes Care (36: 67–74) and research by Rosenbloom AL, Joe JR, Young RS, Winter WE (1999) on the emerging epidemic of type 2 diabetes in youth. It also cites epidemiological studies on diabetic kidney disease, including work by Reutens AT, Prentice L, and Atkins RC (2008). Overall, the document focuses on the epidemiology, complications, and clinical understanding of diabetes mellitus.


## Notes

  -  This project uses the latest modular LangChain packages (langchain-community, langchain-text-splitters, etc.). All required dependencies are listed in requirements.txt to ensure a smooth setup without import errors.

  -  OCR, embeddings, and LLM calls are mocked where required to allow offline execution and avoid external API dependencies.

  - The system architecture supports seamless replacement with real OCR models, embedding APIs, and LLMs.

### Optional UI Note
A Streamlit-based UI was experimented with during development but was excluded from final submission to ensure deterministic execution and avoid state-related reruns common in reactive frameworks. The core RAG system is demonstrated via a CLI-based interface for stability and clarity.

## Optional Enhancements

  - Streamlit UI for document upload and chat interface

  - Replace mock embeddings with real embedding models

  - Deploy as a web service


## Author
### Asra Anjum
