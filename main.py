import discord
from discord.ext import commands
import os
import asyncio

# Get intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'✅ Bot is ready. Logged in as {bot.user}')
    print(f'📊 Bot ID: {bot.user.id}')
    print(f'🔗 Servers: {len(bot.guilds)}')
    print(f'👥 Users: {len(bot.users)}')
    
    # Set bot status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!help'))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="❌ Error",
            description=f"Missing required argument: {error.param}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title="❌ Error",
            description="Invalid argument provided",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    else:
        print(f"Error: {error}")

@bot.event
async def on_guild_join(guild):
    print(f"✅ Joined server: {guild.name} ({guild.id})")

@bot.event
async def on_guild_remove(guild):
    print(f"❌ Left server: {guild.name} ({guild.id})")

async def load_cogs():
    """Load all cogs from the cogs folder"""
    cogs_folder = 'cogs'
    
    if not os.path.exists(cogs_folder):
        os.makedirs(cogs_folder)
        print(f"📁 Created {cogs_folder} folder")
    
    for filename in os.listdir(cogs_folder):
        if filename.endswith('.py'):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f'cogs.{cog_name}')
                print(f"✅ Loaded cog: {cog_name}")
            except Exception as e:
                print(f"❌ Failed to load cog {cog_name}: {e}")

async def main():
    """Load all cogs and start the bot"""
    async with bot:
        await load_cogs()
        
        # Replace 'YOUR_BOT_TOKEN' with your actual token
        TOKEN = os.getenv('DISCORD_BOT_TOKEN', 'YOUR_BOT_TOKEN')
        
        if TOKEN == 'YOUR_BOT_TOKEN':
            print("❌ Please set your bot token in the environment variable DISCORD_BOT_TOKEN")
            return
        
        try:
            await bot.start(TOKEN)
        except Exception as e:
            print(f"❌ Failed to start bot: {e}")

if __name__ == '__main__':
    asyncio.run(main())