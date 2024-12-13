'''
https://docs.llamaindex.ai/en/stable/module_guides/models/llms/usage_custom/

python.exe -m pip install --upgrade pip
python -m venv chatbot
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\AI\Scripts\Activate.ps1

pip install llama-index-llms-openai
pip install llama-index-llms-huggingface
pip install llama-index-llms-huggingface-api
pip install "transformers[torch]" "huggingface_hub[inference]"
pip install python-dotenv
'''

'''
This program uses llama_index and OpenAI to read a txt file
and answer questions. You need tokens from OpenAI
'''

#%%
import os
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from IPython.display import Markdown, display 
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import ServiceContext, set_global_service_context
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.memory import ChatMemoryBuffer
from dotenv import load_dotenv


#%%
load_dotenv()

current_folder = os.getcwd()
documents = SimpleDirectoryReader("data").load_data() #pass name of the folder


# set OpenAI model
llm_openai = OpenAI(temperature=0.1, model="gpt-3.5-turbo", max_tokens=512)
#Settings.llm = OpenAI(temperature=0, model="gpt-3.5-turbo", max_tokens=512)

# Check if indexe sare already made and saved from the data
storage_contex_path = os.path.join(current_folder, "storage")
if os.path.exists(storage_contex_path):
    storage_contex = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context = storage_contex)
else:
    index = VectorStoreIndex.from_documents(documents, llm=llm_openai)
    index.storage_context.persist() #save for future


#query_engine = index.as_query_engine()
#query_engine = index.as_chat_engine()

# response = query_engine.query("WHow many subjects were used in this roject?")
# print(response)


#%%
# Initialize chat store and memory buffer
chat_store_path = os.path.join(current_folder, "chat_store.json")
if os.path.exists(chat_store_path):
    chat_store = SimpleChatStore.from_persist_path(persist_path=chat_store_path)
else:
    chat_store = SimpleChatStore()

chat_memory = ChatMemoryBuffer.from_defaults(
    token_limit=3000,
    chat_store=chat_store,
    chat_store_key="user1",
)

# Create a chat engine with memory
chat_engine = index.as_chat_engine(memory=chat_memory)

# Save chat store for persistence
def save_chat_store():
    chat_store.persist(persist_path=chat_store_path)

#%%
# Start interaction with the chat engine
def chat_with_engine():
    print("Start chatting! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Conversation ended. Saving chat history...")
            save_chat_store()
            break
        response = chat_engine.query(user_input)
        print(f"AI: {response}")

# Run chat interface
chat_with_engine()
