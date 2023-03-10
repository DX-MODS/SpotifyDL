# Copyright (C) 2023 DX_MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import random
from dxbotz.utils.txt import dx
from dxbotz.utils.database import db
from dxbotz import START_PIC


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"π Hai {user.mention} \nπΈ'π π° ππππππππ πππππ πππ πππππππ ππππππππ πππππππ’ ππππ£ππ π’ππππππ πππππ!"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("πΌ π³π΄ππ πΌ", callback_data='dev')
        ],[
        InlineKeyboardButton('π’ ππΏπ³π°ππ΄π', url='https://t.me/dxmodsupdates'),
        InlineKeyboardButton('π πππΏπΏπΎππ', url='https://t.me/DXMODS_Support')
        ],[
        InlineKeyboardButton('π π°π±πΎππ', callback_data='about'),
        InlineKeyboardButton('βΉοΈ π·π΄π»πΏ', callback_data='help')
        ]])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)  

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""π Hai {query.from_user.mention} \nπΈ'π π° ππππππππ πππππ πππ πππππππ ππππππππ πππππππ’ ππππ£ππ π’ππππππ πππππ! """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("πΌ π³π΄ππ πΌ", callback_data='dev')                
                ],[
                InlineKeyboardButton('π’ ππΏπ³π°ππ΄π', url='https://t.me/dxmodsupdates'),
                InlineKeyboardButton('π πππΏπΏπΎππ', url='https://t.me/DXMODS_Support')
                ],[
                InlineKeyboardButton('π π°π±πΎππ', callback_data='about'),
                InlineKeyboardButton('βΉοΈ π·π΄π»πΏ', callback_data='help')
                ]]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=dx.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #β οΈ don't change source code & source link β οΈ #
               InlineKeyboardButton("β£οΈ ππΎπππ²π΄", url="https://github.com/DX-MODS/SpotifyDL")
               ],[
               InlineKeyboardButton("β€οΈβπ₯ π·πΎπ ππΎ πππ΄  β€οΈβπ₯", url='https://youtube.com/@DX-MODS')
               ],[
               InlineKeyboardButton("π π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("βοΈ π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=dx.ABOUT_TXT,            
            reply_markup=InlineKeyboardMarkup( [[
               #β οΈ don't change source code & source link β οΈ #
               InlineKeyboardButton("β£οΈ ππΎπππ²π΄", url="https://github.com/DX-MODS/SpotifyDL")
               ],[
               InlineKeyboardButton("π₯οΈ π·πΎπ ππΎ πΌπ°πΊπ΄", url="https://youtube.com/@DX-MODS")
               ],[
               InlineKeyboardButton("π π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("βοΈ π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=dx.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #β οΈ don't change source code & source link β οΈ #
               InlineKeyboardButton("β£οΈ ππΎπππ²π΄", url="https://github.com/DX-MODS/SpotifyDL")
               ],[
               InlineKeyboardButton("π₯οΈ π·πΎπ ππΎ πΌπ°πΊπ΄", url="https://youtube.com/@DX-MODS")
               ],[
               InlineKeyboardButton("π π²π»πΎππ΄", callback_data = "close"),
               InlineKeyboardButton("βοΈ π±π°π²πΊ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()
