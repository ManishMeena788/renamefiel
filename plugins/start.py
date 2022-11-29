#(©)CodeXBotz
import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot

#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

@Bot.on_message(filters.command('start') & filters.private)
async def Start(client: Client, message: Message):
  await message.reply_text("<b>👤 Admin Pannel</b>")
