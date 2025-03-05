import random
from random import choice, randint
from datetime import datetime
import requests
coin_toss = ["heads", "tails"]
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "It's really silent 🤐..."
    elif 'hello' in lowered:
        return 'Hello 🙏'
    elif 'how are you' in lowered:
        return 'I am doing fine, how are you?'
    elif 'bye' in lowered:
        return 'See you later!'
    elif 'roll d6' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'roll d10' in lowered:
        return f'You rolled: {randint(1, 10)}'
    elif 'roll d20' in lowered:
        return f'You rolled: {randint(1, 20)}'
    elif 'roll d100' in lowered:
        return f'You rolled: {randint(1, 100)}'
    elif 'good morning' in lowered:
        return 'Good morning 🌄'
    elif 'Shush' in lowered:
        return '🤫'
    elif 'good night' in lowered:
        return 'Good Night 🥱.'
    elif len(user_input) >= 200:
        return "That's a really long sentence 🤯"
    elif '🫂' in lowered:
        return '🫂'
    elif "😎" in lowered:
        return '😎'
    elif "ok" in lowered:
        return '👍'
    elif "flip a coin" in lowered:
        return f'{random.choice(coin_toss)}'
    elif 'which country you live in' in lowered:
        return "India"
    elif "hi" in lowered:
        return 'Yo'
    elif "help" in lowered:
        return """These are the list of commands you can use:
1) hello
2) how are you
3) hi
5) good morning
6) bye
7) roll d6
8) roll d10
9) roll d20
10) roll d100
14) flip a coin
15) rickroll 
        """
    elif "rickroll" in lowered:
        return 'https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713'
    else:
        pass
