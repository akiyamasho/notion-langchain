import os

from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
QDRANT_HOST = os.getenv("QDRANT_HOST", "")
assert NOTION_API_KEY, "Please set `NOTION_API_KEY` in .env file"
assert OPENAI_API_KEY, "Please set `OPENAI_API_KEY` in .env file"
assert QDRANT_HOST, "Please set `QDRANT_HOST` in .env file"
