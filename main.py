import discord
from discord.ext import commands, tasks

# замініть 👇 на токен який ви скопіювали
TOKEN = 'Ваш токен'

#створюємо об'єкт бота
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Запуск бота
bot.run(TOKEN)
