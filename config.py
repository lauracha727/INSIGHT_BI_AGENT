import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
KAGGLE_DATASET = os.getenv("KAGGLE_DATASET")
DATABASE_PATH = os.getenv("DATABASE_PATH")
MODEL = os.getenv("MODEL", "gpt-5.5")