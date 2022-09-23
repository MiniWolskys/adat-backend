import os
from dotenv import load_dotenv

load_dotenv()


def get_key(key_name: str) -> str:
    return os.getenv(key_name)
