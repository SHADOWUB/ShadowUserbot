from telethon.sync import TelegramClient, events
import asyncio , telethon.sync
from telethon import TelegramClient, events, Button , functions
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest , GetParticipantRequest
from telethon.tl.functions.messages import ForwardMessagesRequest , SendMessageRequest
from telethon.tl.types import InputPeerChannel ,PeerUser, PeerChat, PeerChannel , ChannelParticipantCreator  ,ChannelParticipantAdmin
from modules.helpers.genai import *

async def gemini_do(event):
    if event.is_reply:
        print(event)
      
