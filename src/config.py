import os
from dotenv import load_dotenv
from openai import OpenAI

#env loading
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

#checking if api_key exists
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables, please ensure .env file in the src folder contains the OPENAI_API_KEY variable with the correct value.")

#creating OPENAI client object
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)