import asyncio
import os

from pyrogram import Client

from config import API_ID, API_HASH, BOT_TOKEN

from utils.logger import logger

from handlers.start import register_handlers as register_start
from handlers.search import register_handlers as register_search
from handlers.pagination import register_handlers as register_pagination

from aiohttp import web

client = Client("discovery_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

register_start(client)
register_search(client)
register_pagination(client)

async def handle(request):
    return web.Response(text="Bot is alive")

async def main():
    logger.info("Starting bot...")
    await client.start()
    logger.info("Bot started.")

    # Health check server for Render
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logger.info(f"Health check server started on port {port}")

    await asyncio.Event().wait()  # Run indefinitely

if __name__ == "__main__":
    asyncio.run(main())
