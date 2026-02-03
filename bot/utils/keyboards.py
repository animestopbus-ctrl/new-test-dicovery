from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from models.channel_model import Channel

def build_results_keyboard(channels: list[Channel], page: int, total_pages: int, keyword: str) -> InlineKeyboardMarkup:
    per_page = 5
    start = (page - 1) * per_page
    end = start + per_page
    page_channels = channels[start:end]

    buttons = []
    for ch in page_channels:
        text = f"{ch.name} | {ch.subscriber_count:,} members"
        url = f"https://t.me/{ch.username}"
        buttons.append([InlineKeyboardButton(text, url=url)])

    pag_row = []
    if page > 1:
        pag_row.append(InlineKeyboardButton("⬅ Prev", callback_data=f"page:{keyword}:{page-1}"))
    pag_row.append(InlineKeyboardButton(f"Page {page}/{total_pages}", callback_data="noop"))
    if page < total_pages:
        pag_row.append(InlineKeyboardButton("Next ➡", callback_data=f"page:{keyword}:{page+1}"))

    if pag_row:
        buttons.append(pag_row)

    return InlineKeyboardMarkup(buttons)
