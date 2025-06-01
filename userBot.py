from telethon import TelegramClient, events
from telethon.tl.types import Channel, Chat

# Replace with your API details
api_id = 20330555
api_hash = '79f0bc3c2ac13b68ede0280576cce4c1'

# This will create a session file named 'session_name.session'
client = TelegramClient('session_name', api_id, api_hash)

# Replace with your source channel titles (exact match)
SOURCE_CHANNEL_TITLE = "DEEP WIN TRADER SVIP's"
SOURCE_CHANNEL_TITLE2 = "PrivateNet"

# Replace with the contact's username or user ID
target_user = '@jayeshlakhani2107'
target_user2 = '@Dhruvpokar1'

@client.on(events.NewMessage())
async def forward_message(event):
    try:
        chat = event.chat
        if isinstance(chat, (Channel, Chat)):
            if chat.title in [SOURCE_CHANNEL_TITLE, SOURCE_CHANNEL_TITLE2]:
                await client.send_message(target_user, event.message)
                await client.send_message(target_user2, event.message)

                print("Message Forward")
        else:
            print(f"Ignored message from non-channel/chat source: {chat}")
    except Exception as e:
        print(f"Error in forward_message: {e}")

client.start()
print("Userbot is running...")
client.run_until_disconnected()
