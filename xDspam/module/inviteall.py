# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @GhostRadha
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @RadhaX2Support
# ɢɪᴛʜᴜʙ :- @GhostRadha ""

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from xDspam import HNDLR, OWNER_ID


@Client.on_message(
    filters.user(OWNER_ID) & filters.command(["scrape", "inviteall"], prefixes=HNDLR)
)
@Client.on_message(
    filters.me & filters.command(["scrape", "inviteall"], prefixes=HNDLR)
)
async def scrape_members(xDspam: Client, message: Message):
    txt = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 1)
    if txt:
        xchat = str(txt[0])
        try:
            cht = await xDspam.get_chat(xchat)
            await xDspam.join_chat(cht.username)
        except Exception as a:
            return await message.reply_text(str(a))
        await message.reply_text(f"inviting users from @{cht.username}")
        added = 0
        async for x in xDspam.get_chat_members(cht.id):
            user = x.user.id
            try:
                await xDspam.add_chat_members(message.chat.id, user)
                added += 1
                await asyncio.sleep(2)
            except Exception as a:
                print(str(a))
        return await xDspam.send_message(
            message.chat.id,
            f"**Users Added!** \nFrom chat: @{cht.username} \nTotal users added: `{added}` \n\n © @RadhaX2Support",
        )
    else:
        await message.reply_text(f"*#Wrong usage** \n syntax: {HNDLR}scrape @chatlink")
