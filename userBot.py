from telethon import TelegramClient, events

# Replace with your API details
api_id = 20330555
api_hash = '79f0bc3c2ac13b68ede0280576cce4c1'

# This will create a session file named 'session_name.session'
client = TelegramClient('session_name', api_id, api_hash)

# Replace with your target channel title (exact match)
SOURCE_CHANNEL_TITLE = "DEEP WIN TRADER SVIP's"  # e.g., channel name, not link
SOURCE_CHANNEL_TITLE2 = "PrivateNet"  # e.g., channel name, not link

# Replace with the contact's username or user ID
target_user = '@jayeshlakhani2107'
# target_user2 = '@Dhruvpokar1'


@client.on(events.NewMessage())
async def forward_message(event):
    if event.chat and (event.chat.title == SOURCE_CHANNEL_TITLE
                       or event.chat.title == SOURCE_CHANNEL_TITLE2):
        await client.send_message(target_user, event.message)
        # await client.send_message(target_user2, event.message)


client.start()
print("Userbot is running...")
client.run_until_disconnected()
