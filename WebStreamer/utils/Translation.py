# This file is a part of FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery


class Language(object):
    class en(object):
        START_TEXT = """
<i>👋 Hᴇʏ,</i>{}\n
<i>I am <b>AutoFileStreamBot</b> As Well As Direct Links Generator. Here i what i do.</i>\n
<i>1, Send me any file (or) forwarded file from telegram.</i>
<i>2, I will generate direct download link and watch link.</i>
<i>If the file is playable, the watch link will stream the file (.mp4 required)</i>
<i>3, This link generated do not expire. </i>
<i>4, Download link with the fastest speed.</i>\n
<b><i>CLICK ON <b>HELP</b> BUTTON BELOW TO GET MORE INFORMATIONS</i>\n</b>
<i><u>⚠️𝗪𝗔𝗥𝗡𝗜𝗡𝗚⚠️</i></u>
<i>🔞SENDING PORNOGRAPHIC CONTENTS TO BOT MAY LEAD TO PERMANENT BAN AND FILE LINK WILL BE REMOVED FROM YOUR SERVER.🔞</i>\n
<b>💰For SUPPORT AND DONATIONS💵</b>
<i>Please contact Developer: 👨‍💻@iamakinola</i>\n"""

        HELP_TEXT = """
<i>I am <b>AutoFileStreamBot</b> As Well As Direct Links Generator. Here i what i do.</i>\n
<i>1, Send me any file (or) forwarded file from telegram.</i>
<i>Be it Videos, Pictures, Musics, Documents(pdf,txt), Games, Softwares,etc </i>
<i>2, I will generate direct download link and watch link</i>
<i>If the file is playable to watch, the watch link will stream the file (.mp4 required)</i>
<i><b>Note: Watch link is generated for every file. But if file is not playable(mp4, mp3), watch link wont work.</i><b>
<i>3, This link generated do not expire. </i>
<i>4, Download link with the fastest speed.</i>
<i>5, Bot supported almost all format.</i></u></i>\n
<i><b>FAQS</i></b>
<i><b>Is my files secure?</b> Yes, 100%</i>
<i><b>How long before link generated expires?</b> Forever maybe</i>
<i><b>What happened when i get Banned?</b> You won't have access to bot again</i>
<i><b>What is the maximum file size i can send to bot?</b> Depend on telegram app </i>
<i><u>⚠️𝗪𝗔𝗥𝗡𝗜𝗡𝗚⚠️</u></i>
<i>🔞SENDING PORNOGRAPHIC CONTENTS TO BOT MAY LEAD TO PERMANENT BAN AND FILE LINK WILL BE REMOVED FROM YOUR SERVER.🔞</i>\n
<b>Need this Bot for your personal project? <b>: <a href='https://t.me/iamakinola'>[ CONTACT US ]</a></b>\n
<b>💰For SUPPORT AND DONATIONS💵</b>
<i>CONTACT DEVELOPER (OR REPORT BUGS</i> <b>: <a href='https://t.me/iamakinola'>[CLICK HERE]</a></b>\n
<i>IS THIS BOT HELPFUL TOOL? </i>  <b>: <a href='https://t.me/tlgrmcbot?start=autofilestreambot-review'>[LEAVE A REVIEW]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ BOT NAME : AutoFileStream</b>\n
<b>🔸VERSION : 3.0.3.1</b>\n
<b>👨‍💻DEVELOPER : olaniyi akinola @iamakinola</b>\n
<b>🔹Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ : [ 09-July-21 ] 12:36 AM</b>
<b>💰For SUPPORT AND DONATIONS💵</b>
<i>CONTACT DEVELOPER (OR REPORT BUGS</i> <b>: <a href='https://t.me/iamakinola'>[CLICK HERE]</a></b>\n
<i>IS THIS BOT HELPFUL TOOL? </i>  <b>: <a href='https://t.me/tlgrmcbot?start=autofilestreambot-review'>[LEAVE A REVIEW]</a></b>"""

        stream_msg_text ="""
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <i>{}</i>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <i>{}</i>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <i>{}</i>\n
<b>🖥WATCH :</b> <i>{}</i>\n
<i>CONTACT DEVELOPER (OR REPORT BUGS</i> <b>: <a href='https://t.me/iamakinola'>[CLICK HERE]</a></b>\n
<i>IS THIS BOT HELPFUL TOOL? </i>  <b>: <a href='https://t.me/tlgrmcbot?start=autofilestreambot-review'>[LEAVE A REVIEW]'></a></b>"""


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
