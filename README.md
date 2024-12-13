# OpenAI-and-Ollama-based-RAG-Engine

![Static Badge](https://img.shields.io/badge/LLM-FF0000)
![Static Badge](https://img.shields.io/badge/Python-8A2BE2)
![Static Badge](https://img.shields.io/badge/RAG-8A2BE2)
![Static Badge](https://img.shields.io/badge/Ollama-4CAF50)
![Static Badge](https://img.shields.io/badge/Hugging%20Face%20Transformer-4CAF50)

This repository contains a chatbot that uses the LlamaIndex library and OpenAI's GPT models for intelligent question-answering based on textual data. The chatbot ingests `.txt` files, processes them into an index, and allows for interactive querying with memory support.

## Features

- **Text File Ingestion**: Reads `.txt` files from a designated folder.
- **Indexing**: Creates and persists a vector-based index using OpenAI embeddings.
- **Memory Support**: Includes memory buffers for conversational context.
- **Interactive Chat**: Provides a terminal-based chat interface for querying indexed documents.
- **Persistence**: Saves chat history and indexes for reusability across sessions.

## Installation

### Prerequisites
- Python 3.8 or later
- OpenAI API key

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv chatbot
   
   # On Windows
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\chatbot\Scripts\Activate.ps1

   # On macOS/Linux
   source chatbot/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   python -m pip install --upgrade pip
   pip install llama-index-llms-openai
   pip install python-dotenv
   ```

4. **Add environment variables**:
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Prepare the Data**:
   - Place all `.txt` files you want to query in a folder named `data` within the project directory.

2. **Run the Script**:
   ```bash
   python chatbot.py
   ```

3. **Interact**:
   - Enter your questions in the terminal.
   - Type `exit` to terminate the session.

## File Structure

```
<repository-name>/
├── data/                 # Directory for .txt files
├── chatbot.py            # Main script
├── .env                  # Environment variables
└── README.md             # Project documentation
```

## Configuration

- **Chatbot Memory**:
  - Memory is managed using a `SimpleChatStore` and `ChatMemoryBuffer`.
  - Adjust `token_limit` and `chat_store_key` in the script as needed.

- **Embedding Model**:
  - The OpenAI GPT model is set to `gpt-3.5-turbo`. You can change it in the script if desired.

## Dependencies

- [LlamaIndex](https://github.com/jerryjliu/llama_index)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- OpenAI GPT models

## Limitations

- Requires an OpenAI API key for operation.
- Designed for `.txt` files; other formats are not supported out of the box.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Built using the LlamaIndex library and OpenAI's GPT models.
