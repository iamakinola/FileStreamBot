# This file is a part of FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


class Language(object):
    class en(object):
        START_TEXT = """
<i>👋 Hᴇʏ,</i>{}\n
<i>I'm File Stream Bot As Well as Direct Links Generator</i>\n
<i>Cʟɪᴄᴋ ᴏɴ Hᴇʟᴘ ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>\n
<b>🔞 SENDING PRONOGRAPHIC CONTENTS TO BOT MAY LEADS TO PERMANENT BAN.🔞</b>\n

        HELP_TEXT = """
<i>- SEND ME A FILE (OR)FORWARED MEDIA FROM TELEGRAM.</i>
<i>- I WILL PROVIVE DIRECT DOWNLOAD LINK AND WATCH LINK !.</i>
<i>- IF THE FILE IS PLAYABLE, THE WATCH LINK WILL STREAM THE FILE.</i>
<i>- LINKS GENERATED DO NOT EXPIRE AND IT CAN BE EMBED TO WEBSITES</i>
<i>- LINKS GENERATED CAN BE STREAM</i>
<i>- DOWNLOAD LINK WITHFASTEST SPEED</i>
<i>- FILE RESOLUTIONS AND SIZE REMAIN THE SAME>
<i>MY LINKS DO NOT EXPIRE AND IT CAN BE EMBED TO WEBSITES</i>\n
<u>🚸𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n
<b>🔞 SENDING PRONOGRAPHIC CONTENTS TO BOT MAY LEADS TO PERMANENT BAN.🔞</b>\n
<i>CONTACT DEVELOPER (OR) REPORT BUG</i> <b>:@iamakinola</b>"""

        ABOUT_TEXT = """
<b>⚜ Mʏ ɴᴀᴍᴇ : Public Link Generator</b>\n
<b>🔸Vᴇʀꜱɪᴏɴ : 3.0.3.1</b>\n
<b>🔹Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ : [ 18-Feb-22 ] 12:36 AM</b>
"""

        stream_msg_text ="""
<b>💰FOR DONATION CONTACT DEVELOPER @iamakinola💰</b>\n
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
