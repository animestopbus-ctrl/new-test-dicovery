from pyrogram import filters
from pyrogram.types import Message

from services.search_service import search_channels
from utils.keyboards import build_results_keyboard
from utils.theme import SEARCH_HEADER, NO_RESULTS, ERROR_MSG
from utils.logger import logger

def register_handlers(client):
    @client.on_message(filters.command("sq"))
    async def search_handler(_: None, message: Message):
        try:
            keyword = " ".join(message.command[1:])
            if not keyword:
                await message.reply("Please provide a keyword.")
                return

            channels = await search_channels(keyword)
            if not channels:
                await message.reply(NO_RESULTS)
                return

            page = 1
            per_page = 5
            total_pages = (len(channels) + per_page - 1) // per_page
            keyboard = build_results_keyboard(channels, page, total_pages, keyword)

            await message.reply(SEARCH_HEADER.format(keyword=keyword), reply_markup=keyboard)
        except Exception as e:
            logger.error(f"Search error: {e}")
            await message.reply(ERROR_MSG)
