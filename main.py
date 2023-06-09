import json
import random

import discord
import poe
from discord import *
from discord.ext import commands

token = json.loads(open('config.json', 'r').read())['token']
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)

models = {
    'claude-v1': 'a2_2',
    'claude-instant': 'a2',
    'claude-instant-100k': 'a2_100k',
    'sage': 'capybara',
    'gpt-4': 'beaver',
    'gpt-3.5-turbo': 'chinchilla',
}


@bot.event
async def on_ready():
    print(f'Бот готов к работе.')


@bot.command(name='test', description='Пинг бота')
async def test(ctx):
    await ctx.send('pong')


@bot.command(name='help', description='Помощь и доступные модели')
async def help(ctx):
    embed = discord.Embed(title='g4f.ai help',
                          description='available models:\n```asm\ngpt-4\ngpt-3.5-turbo\nclaude-v1\nclaude-instant\nclaude-instant-100k\n```\ncommands:\n```asm\n/help\n/create <prompt> <model (default: gpt-4)>\n```',
                          color=8716543)

    await ctx.send(embed=embed)


@bot.command(name='create', description='Промпт для LLM (gpt-4, claude etc...)')
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
        await ctx.send(f'an error occured: {e}')


@bot.slash_command(name="create", description="Создать запрос к модели ChatGPT")
async def create_slash(ctx,
                       prompt: Option(str, description="Промпт для модели"),
                       model: Option(str, "Выберите модель", choices=[
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

        # Собираем все части ответа в одну строку
        response = base
        for token in completion:
            response += token['text_new']

        # Заменяем "Discord Message:" на пустую строку
        response = response.replace('Discord Message:', '')

        # Отправляем собранный ответ одним сообщением
        await ctx.send(response)

    except Exception as e:
        await ctx.send(f'an error occured: {e}')


bot.run(token)
