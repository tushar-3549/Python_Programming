from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# BOT Setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# message functionality

async def send_message(message: Message, user_message: str):
    if not user_message:
        print("Message was empty because intents were not enabled probably")
        return

    is_private = user_message[0] == '?'

    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e) 

# Startup for our BOT
@client.event
async def on_ready():
    print(f'{client.user} is now running ...')

# Handling incoming message
@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    username = message.author
    user_message = message.content
    channel = message.channel

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main():
    client.run(token = TOKEN)

if __name__ == '__main__':
    main()