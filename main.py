# main.py

import discord
from discord.ext import commands

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Start the bot with your token
bot.run('YOUR_BOT_TOKEN')
