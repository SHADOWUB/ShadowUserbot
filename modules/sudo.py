from telethon.sync import TelegramClient, events
import asyncio
from telethon import TelegramClient, events, Button
import telethon.sync
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon import functions
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

async def add_sudo(event):
    await event.reply("SUDO ?")
    
async def sudo_list(event):
    await event.reply("SUDOWODO ?")
