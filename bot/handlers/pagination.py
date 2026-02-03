import re

from pyrogram import filters
from pyrogram.types import CallbackQuery

from services.search_service import search_channels
from utils.keyboards import build_results_keyboard
from utils.logger import logger
from bot.main import client

@client.on_callback_query(filters.regex(r"^page:(.+?):(\d+)$"))
async def pagination_handler(_: None, callback_query: CallbackQuery):
    try:
        match = re.match(r"^page:(.+?):(\d+)$", callback_query.data)
        if not match:
            return

        keyword, page_str = match.groups()
        page = int(page_str)

        channels = await search_channels(keyword)
        per_page = 5
        total_pages = (len(channels) + per_page - 1) // per_page

        if page < 1 or page > total_pages:
            return

        keyboard = build_results_keyboard(channels, page, total_pages, keyword)
        await callback_query.edit_message_reply_markup(keyboard)
    except Exception as e:
        logger.error(f"Pagination error: {e}")