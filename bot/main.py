import asyncio

from pyrogram import Client

from config import API_ID, API_HASH, BOT_TOKEN

from utils.logger import logger

import handlers.start
import handlers.search
import handlers.pagination

client = Client("discovery_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    logger.info("Starting bot...")
    await client.start()
    logger.info("Bot started.")
    await asyncio.Event().wait()  # Run indefinitely

if __name__ == "__main__":
    asyncio.run(main())