import asyncio

from PAKHIMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/e999c40cb700e7c684b75.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ \n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="⎯꯭‌✭𝆺꯭𝅥𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁✭", url=f"https://t.me/InnocentIdkaaa"
            ),
            InlineKeyboardButton(
                text="⎯꯭‌✭𝆺꯭𝅥𝚂𝚄𝙿𝙿𝙾𝚁𝚃✭", url=f"https://t.me/friendship_forever_group143"
            ),
        ],
                [
            InlineKeyboardButton(
                text="⎯꯭‌✭𝆺꯭𝅥𝚄𝙿𝙳𝙰𝚃𝙴✭", url=f"https://t.me/khamosiyaaaan"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "⛧ᴄʟᴏsᴇ⛧", callback_data="close"
                    )
                ],
            ]
        )
    )
