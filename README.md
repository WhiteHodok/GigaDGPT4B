# GigaDGPT4B

This is a Discord bot written in Python that utilizes the discord and poe libraries to interact with users and generate responses using language models. The bot has several commands and features that allow users to test the bot's responsiveness and create prompts for different models.

![image](https://github.com/WhiteHodok/GigaDGPT4B/assets/39564937/fcb59c1b-b86a-4cc2-bbcd-f259b1d1178e)


## Dependencies

```sh
# lib install
pip install -r requirements.txt
```

## Usage 

1. Import the required libraries and modules:

```sh

import json
import random
import discord
import poe
from discord import *
from discord.ext import commands

```

2. Load the bot token from the config.json file and initialize the bot:

```sh

token = json.loads(open('config.json', 'r').read())['token']
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)


```

3. Define the available language models:


```sh
models = {
    'claude-v1': 'a2_2',
    'claude-instant': 'a2',
    'claude-instant-100k': 'a2_100k',
    'sage': 'capybara',
    'gpt-4': 'beaver',
    'gpt-3.5-turbo': 'chinchilla',
}
```

4. Implement the on_ready event handler:

```sh

@bot.event
async def on_ready():
    print(f'Bot is ready.')

```

5. Implement the test command:

```sh

@bot.command(name='test', description='Ping the bot')
async def test(ctx):
    await ctx.send('pong')

```

6. Implement the help command:

```sh
@bot.command(name='help', description='Help and available models')
async def help(ctx):
    embed = discord.Embed(title='g4f.ai help',
                          description='available models:\n```asm\ngpt-4\ngpt-3.5-turbo\nclaude-v1\nclaude-instant\nclaude-instant-100k\n```\ncommands:\n```asm\n/help\n/create <prompt> <model (default: gpt-4)>\n```',
                          color=8716543)

    await ctx.send(embed=embed)
```


