import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def require_env(var_name: str) -> str:
    """
    Retrieves an environment variable or raises an error if missing or empty.
    """
    value = os.getenv(var_name)
    # Check if value is None or an empty string
    if not value:
        raise RuntimeError(f"Missing required environment variable: {var_name}")
    return value

# Required Variables
BOT_TOKEN = require_env("BOT_TOKEN")
API_HASH = require_env("API_HASH")
MONGO_URI = require_env("MONGO_URI")

# API_ID requires specific handling to ensure it is an integer
try:
    API_ID = int(require_env("API_ID"))
except ValueError:
    raise RuntimeError("API_ID environment variable must be a valid integer.")

# Optional (with default)
DB_NAME = os.getenv("DB_NAME", "telegram_bot")