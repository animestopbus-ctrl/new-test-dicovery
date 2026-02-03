from pyrogram import filters
from pyrogram.types import Message

from utils.theme import WELCOME
from bot.main import client  # Import client from main if needed, but decorators register automatically

@client.on_message(filters.command("start") & filters.private)
async def start_handler(_: None, message: Message):
    await message.reply(WELCOME)