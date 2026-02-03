import asyncio

from pyrogram import Client

from config import API_ID, API_HASH, BOT_TOKEN

from utils.logger import logger

from handlers.start import register_handlers as register_start
from handlers.search import register_handlers as register_search
from handlers.pagination import register_handlers as register_pagination

client = Client("discovery_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

register_start(client)
register_search(client)
register_pagination(client)

async def main():
    logger.info("Starting bot...")
    await client.start()
    logger.info("Bot started.")
    await asyncio.Event().wait()  # Run indefinitely

if __name__ == "__main__":
    asyncio.run(main())
