# This file is a part of FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


class Language(object):
    class en(object):
        START_TEXT = """
<i>👋 Hᴇʏ,</i>{}\n
<i>I am <b>AutoFileStreamBot</b> As Well As Direct Links Generator. Here i what i do.</i>\n
<i>1, Send me any file (or) forwarded file from telegram</i>
<i>2, I will generate direct download link and watch link</i>
<i>If the file is playable, the watch link will stream the file (.mp4 required)</i>
<i>3, This link generated do not expire. </i>
<i>4, Download link with the fastest speed</i>\n
<i>CLICK ON HELP BUTTON TO GET MORE INFORMATIONS</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>
<b>🔞SENDING PORNOGRAPHIC CONTENTS TO BOT MAY LEAD TO PERMANENT BAN🔞</b>\n
<b>For support and Donation</b>\n
<i>please contact Developer: @iamakinola</i>\n"""

        HELP_TEXT = """
<i>I am <b>AutoFileStreamBot</b> As Well As Direct Links Generator. Here i what i do.</i>\n
<i>1, Send me any file (or) forwarded file from telegram</i>
<i>2, I will generate direct download link and watch link</i>
<i>If the file is playable, the watch link will stream the file (.mp4 required)</i>
<i>3, This link generated do not expire. </i>
<i>4, Download link with the fastest speed</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>
<b>🔞SENDING PORNOGRAPHIC CONTENTS TO BOT MAY LEAD TO PERMANENT BAN🔞</b>\n
<b>For support and Donation</b>\n
<i>Cᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ (ᴏʀ) ʀᴇᴘᴏʀᴛ ʙᴜɢꜱ</i> <b>: <a href='https://t.me/iamakinola'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ Mʏ ɴᴀᴍᴇ : Public Link Generator</b>\n
<b>🔸Vᴇʀꜱɪᴏɴ : 3.0.3.1</b>\n
<b>🔹Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ : [ 18-Feb-22 ] 12:36 AM</b>
"""

        stream_msg_text ="""
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>\n
<b>🖥WATCH :</b> <i>{}</i>"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close')
        ],
        [InlineKeyboardButton("📢 Bot Channel", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 Bot Channel", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Hᴏᴍᴇ', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('Cʟᴏsᴇ', callback_data='close'),
        ],
        [InlineKeyboardButton("📢 Bot Channel", url=f'https://t.me/{Var.UPDATES_CHANNEL}')]
        ]
    )
