import asyncio
from pytgcalls import idle
from Deepak.main import call_py, bot, tgbot, Test, Deepak

from Deepak import __version__

from os import getenv
from config import LOG_GROUP_ID

START_PIC = "https://telegra.ph/file/3c86a0a10da760aa52a7d.mp4"  
from telethon import Button

Lola = "🥀 Uʟᴛʀᴀ X Mᴜsɪᴄ Bᴏᴛ Hᴀs Bᴇᴇɴ Sᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ...\n\n🥀 ᴏᴡɴᴇʀ [ᴏᴡɴᴇʀ](t.me/OFFICIALHACKERERA)\n\n🥀 Bᴏᴛ Vᴇʀsɪᴏɴ 0.9.5"



async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    await Deepak.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await call_py.start()
    await Test.join_chat("Bhutiya_Haveli")
    await Test.join_chat("Broken_Heart_72")
    await Test.join_chat("OFFICIALHACKER789")
    await Test.join_chat("OFFICIALHACKER8")
    await tgbot.send_file(LOG_GROUP_ID,
                                  START_PIC,
                                  caption=Lola,
                                  buttons=[[Button.url("🥀 Uᴘᴅᴀᴛᴇs", "https://t.me/Broken_Heart_72"),Button.url("🥀 Sᴜᴘᴘᴏʀᴛ", "https://t.me/Bhutiya_Haveli"),]])        
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
tgbot.run_until_disconnected()
