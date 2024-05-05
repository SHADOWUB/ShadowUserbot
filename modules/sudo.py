from telethon.sync import TelegramClient, events
import asyncio , telethon.sync
from telethon import TelegramClient, events, Button , functions
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest , GetParticipantRequest
from telethon.tl.functions.messages import ForwardMessagesRequest , SendMessageRequest
from telethon.tl.types import InputPeerChannel ,PeerUser, PeerChat, PeerChannel , ChannelParticipantCreator  ,ChannelParticipantAdmin

async def add_sudo(event):
    susersf=open("users.txt",'r')
    try:
        susers=susersf.readlines()[0].split(" ")
    except:
        print("no sudo users found")
        return 
    stext=""
    for i in range(len(susers)):
        stext+f"\n{susers[i]}"
    await event.reply("SUDO ?")

async def sudo_list(event):
    susersf=open("users.txt",'r')
    try:
        susers=susersf.readlines()[0].split(" ")
    except:
        await event.reply("No Sudo Users Found")
        return 
    stext=""
    for i in range(len(susers)):
        stext+f"\n{susers[i]}"
    await event.reply("SUDO USERS : \n"+stext)