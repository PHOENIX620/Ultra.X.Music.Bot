import asyncio
from pytgcalls import PyTgCalls
from Deepak.main import call_py, bot, tgbot, Test, Deepak
from Deepak import __version__
from os import getenv
from config import LOG_GROUP_ID
from telethon import Button

START_PIC = "https://telegra.ph/file/3c86a0a10da760aa52a7d.mp4"  
Lola = "🥀 Uʟᴛʀᴀ X Mᴜsɪᴄ Bᴏᴛ Hᴀs Bᴇᴇɴ Sᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ...\n\n🥀 ᴏᴡɴᴇʀ [ᴏᴡɴᴇʀ](t.me/OFFICIALHACKERERA)\n\n🥀 Bᴏᴛ Vᴇʀsɪᴏɴ 0.9.5"

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    await Deepak.start()
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    
    try:
        # Join required chats
        await Test.join_chat("Bhutiya_Haveli")
        await Test.join_chat("Broken_Heart_72")
        await Test.join_chat("OFFICIALHACKER789")
        await Test.join_chat("OFFICIALHACKER8")
    except Exception as e:
        print(f"[ERROR]: Failed to join chat - {str(e)}")
        return
    
    try:
        # Send start message and media with buttons
        await tgbot.send_file(LOG_GROUP_ID,
                              START_PIC,
                              caption=Lola,
                              buttons=[[Button.url("🥀 Uᴘᴅᴀᴛᴇs", "https://t.me/Broken_Heart_72"),
                                        Button.url("🥀 Sᴜᴘᴘᴏʀᴛ", "https://t.me/Bhutiya_Haveli")]])
    except Exception as e:
        print(f"[ERROR]: Failed to send start message - {str(e)}")
        return
    
    await idle()  # Keep the bot alive
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()

# Run the bot with an event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

# Keep running tgbot until disconnected
tgbot.run_until_disconnected()
