# ""ᴅᴇᴀʀ ᴘʀᴏ ᴘᴇᴏᴘʟᴇ,  ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ & ᴄʜᴀɴɢᴇ ᴛʜɪꜱ ʟɪɴᴇ
# ᴛɢ :- @GhostRadha
# ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ :- @RadhaX2Support
# ɢɪᴛʜᴜʙ :- @GhostRadha ""

import asyncio
from random import choice

from pyrogram import Client, filters
from pyrogram.types import Message

from xDspam import HNDLR, LOGS_CHANNEL, OWNER_ID, SUDO_USERS
from xDspam.data import *

usage = f"** ❌ Wrong Usage ❌** \n Type `{HNDLR}help spam`"


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], prefixes=HNDLR))
async def raid(xspam: Client, e: Message):
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(HNY) == 2:
        counts = int(HNY[0])
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        ok = await xspam.get_users(HNY[1])
        id = ok.id
        if int(id) in RadhaX2Support:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is Owner Of this Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is a sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.3)
    elif e.reply_to_message:
        # msg_id = e.reply_to_message.message_id
        counts = int(HNY[0])
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        # HNY = xspam.get_messages(e.chat.id, msg_id)
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if int(id) in RadhaX2Support:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is Owner Of this Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is a sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = choice(RAID)
                msg = f"{mention} {reply}"
                await xspam.send_message(e.chat.id, msg)
                await asyncio.sleep(0.3)
    else:
        await e.reply_text(usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


RUSERs = []


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["rraid", "replyraid"], prefixes=HNDLR)
)
async def rraid(xspam: Client, e: Message):
    global RUSERs
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if HNY:
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        ok = await xspam.get_users(HNY[0])
        id = ok.id
        if int(id) in RadhaX2Support:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is Owner Of this Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is a sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            RUSERs.append(id)
            mention = f"[{fname}](tg://user?id={id})"
            msg = f"Reply Raid Activated Successfully On User {mention}"
            await e.reply_text(msg)
    elif e.reply_to_message:
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if int(id) in RadhaX2Support:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is Owner Of this Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is a sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            RUSERs.append(id)
            mention = f"[{fname}](tg://user?id={id})"
            msg = f"Reply Raid Activated Successfully On User {mention}"
            await e.reply_text(msg)
    else:
        await e.reply_text(usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f"Activated Reply Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["draid", "dreplyraid"], prefixes=HNDLR)
)
async def draid(xspam: Client, e: Message):
    global RUSERs
    HNY = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if HNY:
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        ok = await xspam.get_users(HNY[0])
        id = ok.id
        if int(id) in RadhaX2Support:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is Owner Of this Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is a sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            RUSERs.remove(id)
            mention = f"[{fname}](tg://user?id={id})"
            msg = "Reply Raid Deactivated Successfully"
            await e.reply_text(msg)
    elif e.reply_to_message:
        if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        if int(id) in RadhaX2Support:
            text = f"I can't raid on @RadhaX2Support Owner"
            await e.reply_text(text)
        elif int(id) == OWNER_ID:
            text = f"This guy is Owner Of this Bots."
            await e.reply_text(text)
        elif int(id) in SUDO_USERS:
            text = f"This guy is a sudo user."
            await e.reply_text(text)
        else:
            fname = ok.first_name
            RUSERs.remove(id)
            mention = f"[{fname}](tg://user?id={id})"
            msg = "Reply Raid Deactivated Successfully"
            await e.reply_text(msg)
    else:
        await e.reply_text(usage)
    if LOGS_CHANNEL:
        try:
            await xspam.send_message(
                LOGS_CHANNEL,
                f" Deactivated Reply Raid By User: {e.from_user.id} \n\n User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


REACT_ON = []


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["replyreact"], prefixes=HNDLR)
)
async def react_reply(xspam: Client, message: Message):
    global REACT_ON
    if not message.reply_to_message:
        return
    else:
        user = message.reply_to_message.from_user.id
        REACT_ON.append(user)
        await message.reply_text(
            f"Reply Reaction activated on {message.reply_to_message.from_user.mention}."
        )


@Client.on_message(~filters.me & filters.incoming)
async def watcher(xspam: Client, msg: Message):
    global RUSERs
    global REACT_ON
    id = msg.from_user.id
    if int(id) in RUSERs:
        reply = choice(REPLYRAID)
        await msg.reply_text(reply)
    elif int(id) in REACT_ON:
        await xspam.send_reaction(
            chat_id=msg.chat.id,
            message_id=msg.id,
            emoji="❤️",
        )
