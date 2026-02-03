from pyrogram import filters
from pyrogram.types import Message

from utils.theme import WELCOME

def register_handlers(client):
    @client.on_message(filters.command("start") & filters.private)
    async def start_handler(_: None, message: Message):
        await message.reply(WELCOME)
