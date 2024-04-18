from telethon import *
from telethon.sync import *
import asyncio
from modules.base import outgoing_commands, edited_handler

api_id = 1992385
api_hash = "a470b85e27ed03b83571c42c499da412"
bot_token='5891017864:AAEsJkCGk5hQ-1AZh4Vm14qajhhbhXx9Z-M'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def start_client(session_name):
    client = TelegramClient(session_name, api_id, api_hash)
    try:
        await client.start()
    except:
        print(client_name+" ded")
        return None
    me = await client.get_me()
    ownerid = me.id
    await client.get_dialogs() # cache all chats so it wont cause troubles like chat not found
    
    @client.on(events.NewMessage(outgoing=True))
    async def outgoing_messages(event):
        await outgoing_commands(event)

    @client.on(events.MessageEdited)
    async def editing_messages(event):
        await edited_handler(event)

    await client.run_until_disconnected()


async def main():
    clientlist = ["session"]
    tasks = [start_client(client_name) for client_name in clientlist]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
