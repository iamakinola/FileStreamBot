# Generate Text, Stream Link, reply_markup
async def gen_link(m: Message,log_msg: Messages, from_channel: bool):
    """Generate Text for Stream Link, Reply Text and reply_markup"""
    lang = Language(m)
    file_name = get_name(log_msg)
    file_size = humanbytes(get_media_file_size(log_msg))

    page_link = f"{Var.URL}watch/{get_hash(log_msg)}{log_msg.id}"
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    Stream_Text=lang.stream_msg_text.format(file_name, file_size, stream_link, page_link)
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖥STREAM", url=page_link), InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ 📥", url=stream_link)]])

    if from_channel:
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖥STREAM", url=page_link), InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ 📥", url=stream_link)]])
    else:
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🖥STREAM", url=page_link), InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ 📥", url=stream_link)],
            [InlineKeyboardButton("❌ Delete Link", callback_data=f"msgdelconf2_{log_msg.id}_{get_media_file_unique_id(log_msg)}")]])

    return reply_markup, Stream_Text, stream_link
