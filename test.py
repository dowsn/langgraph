import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load environment variables from a .env file
load_dotenv()

# Access the OPENAI_API_KEY environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
  print("OPENAI_API_KEY not found. Please set it in your .env file.")
  exit(1)

gpt4o_chat = ChatOpenAI(model="gpt-4o", temperature=0)
gpt35_chat = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

msg = HumanMessage(content="Hello world", name="Lance")

# Message list
messages = [msg]

# Invoke the model with a list of messages
response = gpt4o_chat.invoke(messages)
print(response)
