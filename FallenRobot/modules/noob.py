

# Dear Pro  , Don't Remove This Line
# Tg @pythonxgamer
# zen bot @zenxrobot
#Github :- Adityakjha1



import asyncio
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)


from FallenRobot import pbot as bot

Zen = "https://te.legra.ph/file/49b0000f95b740904aeaa.jpg"


@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Zen,
        caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 ᴢᴇɴ  ʀᴏʙᴏᴛ 」](t.me/Zenxrobot)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/pythonxgamer"),
                ]
            ]
        ),
    )


__mod_name__ = "Oᴡɴᴇʀ"
