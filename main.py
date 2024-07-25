from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import requests


# step 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('TOKEN')
# print(TOKEN)

# step 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# step 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled probably)")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


# step 3: HANDLING THE STARTUP FOR OUR BOT

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# step 4: HANDLING INCOMING MESSAGES

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

    if message.content.startswith('!age'):
        name = message.content[len('!age '):]
        response = requests.get(f"YOUR AGIFY.IO API")
        data = response.json()
        age = data["age"]
        await message.channel.send(f'Hello, {name} your age is {age} years old 🧓!')

    if message.content.startswith('!gender'):
        name = message.content[len('!gender '):]
        response = requests.get(f"YOUR GENDERIZE.IO API")
        data = response.json()
        gender = data["gender"]
        await message.channel.send(f'Hello, {name} your gender is {gender}!')

# step 5: MAIN ENTRY POINT

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
