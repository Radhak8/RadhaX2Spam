# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @GhostRadha
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @RadhaX2Support
# ɢɪᴛʜᴜʙ :- @GhostRadha ""

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from xDspam import ALIVE_PIC

Pic = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/84351002f7dd488a17abb.jpg"
Hn = "/"
btn = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("• Channel •", url="https://t.me/RadhaX2Update"),
            InlineKeyboardButton("• Support •", url="https://t.me/RadhaX2Support"),
        ],
        [
            InlineKeyboardButton(
                "• Repo •", url="https://github.com/Radhak8/RadhaX2Spam"
            )
        ],
    ]
)


@Client.on_message(
    filters.private & filters.incoming & filters.command(["start"], prefixes=Hn)
)
async def _start(_, ok: Message):
    msg = f"**Hello [{ok.from_user.first_name}](tg://user?id={ok.from_user.id}) !** \n\n __ • I'm Radha An Advance Spambot__ \n\n **Click Below Buttons for More Info**"
    if ".jpg" in Pic or ".png" in Pic:
        await ok.reply_photo(Pic, caption=msg, reply_markup=btn)
    if ".mp4" in Pic or ".MP4," in Pic:
        await ok.reply_video(Pic, caption=msg, reply_markup=btn)
