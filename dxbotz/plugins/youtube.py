# Copyright (C) 2024 DX-MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

from os import mkdir
from random import randint
from config import AUTH_CHATS, LOG_GROUP, LOGGER
from dxbotz import Dxbotz
from pyrogram import filters
from dxbotz.utils.ytdl import getIds,ytdl_down,audio_opt,thumb_down

@Dxbotz.on_message(filters.regex(r'(https?:\/\/(?:www\.)?youtu\.?be(?:\.com)?\/.*)') & filters.incoming| filters.command(["yt","ytd","ytmusic"]) & filters.regex(r'(https?:\/\/(?:www\.)?youtu\.?be(?:\.com)?\/.*)') & filters.incoming)
async def _(_,message):
    m = await message.reply_text("Gathering information... Please Wait.")
    link = message.matches[0].group(0)
    if link in [
        "https://youtube.com/",
        "https://youtube.com",
        "https://youtu.be/",
        "https://youtu.be",
    ]:
        return await m.edit_text("Please send a valid playlist or video link.")
    elif "channel" in link or "/c/" in link:
        return await m.edit_text("**Channel** Download Not Available. ")
    try:
        ids = await getIds(message.matches[0].group(0))
        videoInPlaylist = len(ids)
        randomdir = "/tmp/"+str(randint(1,100000000))
        mkdir(randomdir)
        for id in ids:
            PForCopy = await message.reply_photo(f"https://i.ytimg.com/vi/{id[0]}/hqdefault.jpg",caption=f"🎧 Title : `{id[3]}`\n🎤 Artist : `{id[2]}`\n💽 Track No : `{id[1]}`\n💽 Total Track : `{videoInPlaylist}`")
            fileLink = await ytdl_down(audio_opt(randomdir,id[2]),id[0])
            thumnail = await thumb_down(id[0])
            AForCopy = await message.reply_audio(fileLink,caption=f"[{id[3]}](https://youtu.be/{id[0]}) - {id[2]}",title=id[3].replace("_"," "),performer=id[2],thumb=thumnail,duration=id[4])
            if LOG_GROUP:
                await PForCopy.copy(LOG_GROUP)
                await AForCopy.copy(LOG_GROUP)
        await m.delete()
    except Exception as e:
        LOGGER.error(e)
        await m.edit_text(e)
