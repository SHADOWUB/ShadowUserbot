from telethon.sync import TelegramClient, events
import asyncio , telethon.sync
from telethon import TelegramClient, events, Button , functions
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest , GetParticipantRequest
from telethon.tl.functions.messages import ForwardMessagesRequest , SendMessageRequest
from telethon.tl.types import InputPeerChannel ,PeerUser, PeerChat, PeerChannel , ChannelParticipantCreator  ,ChannelParticipantAdmin

async def alive_hdlr(event):
    await event.reply("ALIVE",file="https://graph.org/file/0afb5f356a3836220a029.mp4")
