from telethon import *
from telethon.sync import *
import asyncio

api_id = 1992385
api_hash = "a470b85e27ed03b83571c42c499da412"
bot_token='5891017864:AAEsJkCGk5hQ-1AZh4Vm14qajhhbhXx9Z-M'

C=TelegramClient('session',api_id,api_hash)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@C.on(events.NewMessage(outgoing=True,pattern='\.work'))
async def worker(event):
    chat = await event.get_chat()
    await C.send_message(chat,f"WORKING")

 
C.start()
C.run_until_disconnected()