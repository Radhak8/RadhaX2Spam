# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @GhostRadha
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @RadhaX2Support
# ɢɪᴛʜᴜʙ :- @GhostRadha ""

import asyncio
import re
from random import choice

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from xDspam import HNDLR, LOGS_CHANNEL, OWNER_ID, SUDO_USERS
from xDspam.data import *

usage = f"** ❌ Wrong Usage ❌** \n Type `{HNDLR}help spam`"


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["delayspam"], prefixes=HNDLR)
)
async def delayspam(xspam: Client, e: Message):
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    HNYop = HNY[1:]
    if len(HNYop) == 2:
        counts = int(HNYop[0])
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        msg = str(HNYop[1])
        if re.search(Owners.lower(), msg.lower()):
            return await e.reply_text(usage)(
                "**Sorry !!** I can't Spam On @RadhaX2Support owner"
            )
        sleeptime = float(HNY[0])
        if e.reply_to_message:
            reply_to_id = e.reply_to_message.message_id
            for _ in range(counts):
                await xspam.send_message(
                    e.chat.id, msg, reply_to_message_id=reply_to_id
                )
                await asyncio.sleep(sleeptime)
            return
        for _ in range(counts):
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(sleeptime)
    else:
        await e.reply_text(usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Delay Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg} \n Delay Time: {sleeptime}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["ispam", "inlinespam"], prefixes=HNDLR)
)
async def ispam(xspam: Client, e: Message):
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(HNY) == 2:
        counts = int(HNY[0])
        x = await xspam.get_users(HNY[1])
    elif e.reply_to_message:
        counts = int(HNY[0])
        e.reply_to_message.from_user.id
        x = await xspam.get_users(user_id)
    else:
        return await e.reply_text(usage)
    id = x.id
    if int(id) in EnoughBio:
        text = f"I can't raid on @RadhaX2Support Owner"
        await e.reply_text(text)
    elif int(id) == OWNER_ID:
        text = f"This guy is Owner Of this Bots."
        await e.reply_text(text)
    elif int(id) in SUDO_USERS:
        text = f"This guy is a sudo user."
        await e.reply_text(text)
    else:
        fname = x.first_name
        link = choice(PORM)
        mention = f"[{fname}](tg://user?id={id})"
        for _ in range(counts):
            reply = choice(RAID)
            msg = f"{mention} {reply}"
            btn = InlineKeyboardMarkup(
                [[InlineKeyboardButton(f"{fname} Mom's porno", url=f"{link}")]]
            )
            await xspam.send_message(e.chat.id, msg, reply_markup=btn)
            await asyncio.sleep(0.3)

    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Inline Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["pornspam"], prefixes=HNDLR)
)
async def pornspam(xspam: Client, e: Message):
    counts = e.command[1]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
        return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    HNY = "**#Pornspam**"
    count = int(counts)
    for _ in range(count):
        prn = choice(PORM)
        if ".jpg" in prn or ".png" in prn:
            await xspam.send_photo(e.chat.id, prn, caption=HNY)
            await asyncio.sleep(0.4)
        if ".mp4" in prn or ".MP4," in prn:
            await xspam.send_video(e.chat.id, prn, caption=HNY)
            await asyncio.sleep(0.4)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Porn Spam By User: {e.from_user.id} \n Chat: {e.chat.id} \n Counts: {count}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(SUDO_USERS)
    & filters.command(["fspam", "fastspam", "spam", "bigspam"], prefixes=HNDLR)
)
async def spam(xspam: Client, e: Message):
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(HNY) == 2:
        counts = int(HNY[0])
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        msg = str(HNY[1])
        if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!** I can't Spam On @EnoughBio's owner")
        if e.reply_to_message:
            reply_to_id = e.reply_to_message.message_id
            for _ in range(counts):
                await xspam.send_message(
                    e.chat.id, msg, reply_to_message_id=reply_to_id
                )
                await asyncio.sleep(0.3)
            return
        for _ in range(counts):
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.3)
    else:
        await e.reply_text(usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts} \n Spam Message: {msg}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["hang"], prefixes=HNDLR))
async def hang(xspam: Client, e: Message):
    counts = e.command[1]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
        return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    HNY = "⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰"
    count = int(counts)
    for _ in range(count):
        await xspam.send_message(e.chat.id, HNY)
        await asyncio.sleep(0.3)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Hang Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {count}",
            )
        except Exception as a:
            print(a)


WORD = [
    "AJA",
    "TERI",
    "MAA",
    "KI",
    "CHUT",
    "FAAD",
    "DUNGA",
    "HIJDE",
    "TERA",
    "BAAP",
    "HU",
    "KIDXX",
    "SPEED",
    "PAKAD",
    "BHEN KE LAUDE",
    "AA BETA",
    " ADITYA",
    "AAGYA",
    "TERI",
    "MAA ",
    "CHODNE",
    "AB",
    "TERI ",
    "MAA",
    "CHUDEGI",
    "KUTTE",
    "KI",
    "TARAH",
    "BETA",
    "TERI",
    "MAA",
    "KE",
    "BHOSDE",
    "ME",
    "JBL",
    "KE",
    "SPEAKER",
    "DAAL",
    "KAR",
    "BASS",
    "BOOSTED",
    "SONG",
    "SUNUNGA",
    "PURI",
    "RAAT",
    "LAGATAR",
    "TERI",
    "MAA",
    "KE",
    "SATH",
    "SEX",
    "KARUNGA🔥",
    "TERI",
    "MAA",
    "KE",
    "BOOBS",
    "DABAUNGA",
    "XXX",
    "TERI",
    "MAA",
    "KAA",
    "CHUT",
    "MARU",
    "RANDI",
    "KEE",
    "PILEE",
    "TERI",
    "MAA",
    "KAA",
    "BHOSDAA",
    "MARU",
    "SUAR",
    "KEE",
    "CHODE",
    "TERI",
    "MAAA",
    "KEEE",
    "NUDES",
    "BECHUNGA",
    "RANDI",
    "KEE",
    "PILLE",
    "TERI",
    "MAAA",
    "CHODU",
    "SUAR",
    "KEEE",
    "PILEE",
    "TERIII",
    "MAAA",
    "DAILYY",
    "CHUDTTI",
    "HAII",
    "MADHARCHOD",
    "AUKAT",
    "BANAA",
    "LODE",
    "TERAA",
    "BAAP",
    "HUU",
    "TERI",
    "GFF",
    "KAA",
    "BHOSDAA",
    "MARUU",
    "MADHARCHOD",
    "TERI ",
    "NANAI",
    "KAA",
    "CHUTT",
    "MARU",
    "TERII",
    "BEHEN",
    "KAAA",
    "BHOSDAA",
    "MARU",
    "RANDII",
    "KEEE",
    "CHODE",
    "TERI",
    "DADI",
    "KAAA",
    "BOOR",
    "GARAM",
    "KARR",
    "TERE",
    "PUREE",
    "KHANDAN",
    "KOOO",
    "CHODUNGAA",
    "BAAP",
    "SEE",
    "BAKCHODI",
    "KAREGAA",
    "SUARR",
    "KEEE",
    "PILLEE",
    "NAAK",
    "MEEE",
    "NETAA",
    "BAAP",
    "KOO",
    "KABHII",
    "NAAH",
    "BOLNAA",
    "BETAA",
    "CHUSS",
    "LEEE",
    "MERAA",
    "LODAA",
    "JAISE",
    "ALUU",
    "KAAA",
    "PAKODAA",
    "TERI",
    "MAAA",
    "BEHEN",
    "GFF",
    "NANI",
    "DIIN",
    "RAAT",
    "SOTEE",
    "JAGTEE",
    "PELTAA",
    "HUUU",
    "LODEE",
    "CHAAR",
    "CHAWNII",
    "GHODEE",
    "PEEE",
    "TUMM",
    "MEREE",
    "LODEE",
    "PEE",
    "TERI",
    "MAA",
    "KAAA",
    "BOOBS",
    "DABATA HU",
]


uusage = f"** ❌ Wrong Usage ❌** \n Type `{HNDLR}help extra`"
unlimited = False


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["uspam"], prefixes=HNDLR)
)
@Client.on_message(filters.me & filters.command(["uspam"], prefixes=HNDLR))
async def uspam(xspam: Client, e: Message):
    global unlimited
    unlimited = True
    if int(e.chat.id) in GROUP:
        return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    msg = str(e.text[6:])
    if re.search(Owners.lower(), msg.lower()):
        return await e.reply("**Sorry !!** I can't Spam On @RadhaX2Support owner")
    try:
        while unlimited == True:
            await xspam.send_message(e.chat.id, msg)
    except Exception as ex:
        print(ex)
        await e.reply_text(f" Error -! \n\n {ex}")

    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Unlimited Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Spam Message: {msg}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["uraid"], prefixes=HNDLR)
)
@Client.on_message(filters.me & filters.command(["uraid"], prefixes=HNDLR))
async def uraid(xspam: Client, e: Message):
    global unlimited
    unlimited = True
    HNY = e.text[6:]
    if HNY:
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        ok = await xspam.get_users(HNY)
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is the Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            try:
                while unlimited == True:
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
            except Exception as f:
                print(f)
                await e.reply_text(f" Error -! \n\n {f}")

    elif e.reply_to_message:
        # msg_id = e.reply_to_message.message_id
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        # HNY = xspam.get_messages(e.chat.id, msg_id)
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if int(id) in EnoughBio:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy the Owner Of these Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            try:
                while unlimited == True:
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
            except Exception as f:
                print(f)
                await e.reply_text(f" Error -! \n\n {f}")
    else:
        await e.reply_text(uusage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["abuse"], prefixes=HNDLR)
)
@Client.on_message(filters.me & filters.command(["abuse"], prefixes=HNDLR))
async def abuse(xspam: Client, e: Message):
    sex = e.text[7:]
    if sex:
        counts = int(sex)
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        for _ in range(counts):
            msg = choice(WORD)
            await xspam.send_message(e.chat.id, msg)
            await asyncio.sleep(0.001)
    else:
        global unlimited
        unlimited = True
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        try:
            while unlimited == True:
                msg = choice(WORD)
                await xspam.send_message(e.chat.id, msg)
        except Exception as ex:
            print(ex)
            await e.reply_text(f" Error -! \n\n {ex}")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["stop"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["stop"], prefixes=HNDLR))
async def stop(_, e: Message):
    global unlimited
    unlimited = False
    await e.reply_text("Stopped Unlimited Spam/Raid/abuse -;")
