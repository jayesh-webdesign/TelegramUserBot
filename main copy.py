# Userbot script


from telethon import TelegramClient, events

# Replace with your API details
api_id = 20330555
api_hash = '79f0bc3c2ac13b68ede0280576cce4c1'

# This will create a session file named 'session_name.session'
client = TelegramClient('session_name', api_id, api_hash)

# Replace with your target channel username or ID
source_channel = 'https://t.me/+hG1fm1-0rRNiOTE9'  # or channel ID

# Replace with the contact's username or user ID
target_user = '@jayeshlakhani2107'  # or their Telegram ID

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    await client.send_message(target_user, event.message)

client.start()
print("Userbot is running...")
client.run_until_disconnected()
