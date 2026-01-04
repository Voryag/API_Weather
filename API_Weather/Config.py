import os
from dotenv import load_dotenv


load_dotenv("token.env")


API_KEY = os.getenv("API_KEY")