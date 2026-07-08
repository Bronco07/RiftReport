import os
from dotenv import load_dotenv

result = load_dotenv()
print("load_dotenv found a file:", result)

API_KEY = os.getenv("RIOT_API_KEY")
print(API_KEY)