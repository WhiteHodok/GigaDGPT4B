# GigaDGPT4B

ATTENTION : if you have error (an error occured: Invalid token or no bots are available.) , give new token in (https://discord.gg/RHNeeK8k) and input to tokens.txt , if this dont work - i didnt know how this fix , you can try create a vevnv for python and start a bot from venv. Discussion for my problem (https://github.com/xtekky/gpt4free-discord/issues/4)

This is a Discord bot written in Python that utilizes the discord and poe libraries to interact with users and generate responses using language models. The bot has several commands and features that allow users to test the bot's responsiveness and create prompts for different models.

![image](https://github.com/WhiteHodok/GigaDGPT4B/assets/39564937/fcb59c1b-b86a-4cc2-bbcd-f259b1d1178e)

![dream_TradingCard (1)](https://github.com/WhiteHodok/GigaDGPT4B/assets/39564937/052a57f1-c374-4762-ae27-415b8059fe24)


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

7. Implement the say command:

```sh
@bot.command(name='create', description='Prompt for LLM (gpt-4, claude etc...)')
async def say(ctx, prompt: str, model: str = 'gpt-4'):
    try:
        print(ctx.author.name, prompt, model)

        base = f'*model*: `{model}`\n'
        system = 'system: your response will be rendered in a discord message, include language hints when returning code like: ```py ...```, and use * or ** or > to create highlights ||\n prompt: '

        token = random.choice(open('tokens.txt', 'r').read().splitlines())
        client = poe.Client(token.split(':')[0])

        await ctx.send(base)
        base += '\n'

        completion = client.send_message(models[model],
                                         system + prompt, with_chat_break=True)

        for token in completion:
            base += token['text_new']

            base = base.replace('Discord Message:', '')
            await ctx.send(base)

    except Exception as e:
        await ctx.send(f'an error occurred: {e}')

```

8. Implement the create_slash command for slash commands:

```sh
@bot.slash_command(name="create", description="Create a query to the ChatGPT model")
async def create_slash(ctx,
                       prompt: Option(str, description="Prompt for the model"),
                       model: Option(str, "Choose a model", choices=[
                           OptionChoice(name='gpt-4', value='gpt-4'),
                           OptionChoice(name='gpt-3.5-turbo', value='gpt-3.5-turbo'),
                           OptionChoice(name='claude-v1', value='claude-v1'),
                           OptionChoice(name='claude-instant', value='claude-instant'),
                           OptionChoice(name='claude-instant-100k', value='claude-instant-100k'),
                           OptionChoice(name='sage', value='sage'),
                       ])):
    try:
        print(ctx.author.name, prompt, model)

        base = f'*model*: `{model}`\n'
        system = 'system: your response will be rendered in a discord message, include language hints when returning code like: ```py ...```, and use * or ** or > to create highlights ||\n prompt: '

        token = random.choice(open('tokens.txt', 'r').read().splitlines())
        client = poe.Client(token.split(':')[0])

        completion = client.send_message(models[model],
                                         system + prompt, with_chat_break=True)

        # Combine all response parts into a single string
        response = base
        for token in completion:
            response += token['text_new']

        # Replace "Discord Message:" with an empty string
        response = response.replace('Discord Message:', '')

        # Send the assembled response as a single message
        await ctx.send(response)

    except Exception as e:
        await ctx.send(f'an error occurred: {e}')

```

9. Run the BOT:

```sh
bot.run(token)
```


Make sure to provide the necessary prerequisites and follow the installation steps before running the bot. You can customize the command prefix, available models, and modify the code as needed for your specific use case.
