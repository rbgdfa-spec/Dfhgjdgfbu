import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def eight_ball(self, ctx, *, question):
        responses = ["Yes", "No", "Maybe", "Definitely", "I wouldn't count on it."]
        await ctx.send(random.choice(responses))

    @commands.command(name='clap')
    async def clap(self, ctx, *, message):
        await ctx.send(" 👏 ".join(message.split()))

    @commands.command(name='rate')
    async def rate(self, ctx, *, item):
        rating = random.randint(1, 10)
        await ctx.send(f"I rate **{item}** a **{rating}/10**!")

    @commands.command(name='meme')
    async def meme(self, ctx):
        await ctx.send("Here is a meme!")  # Ideally, you'd integrate a meme API.

    @commands.command(name='joke')
    async def joke(self, ctx):
        await ctx.send("Why don't scientists trust atoms? Because they make up everything!")  # Example joke

    @commands.command(name='flip')
    async def flip(self, ctx):
        result = random.choice(["Heads", "Tails"])
        await ctx.send(result)

    @commands.command(name='roll')
    async def roll(self, ctx, num: int = 6):
        result = random.randint(1, num)
        await ctx.send(f"You rolled a {result}")

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send("Pong! 🏓")

    @commands.command(name='avatar')
    async def avatar(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(member.avatar_url)

    @commands.command(name='userinfo')
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        user_info = f"Username: {member.name}\nID: {member.id}"
        await ctx.send(user_info)


def setup(bot):
    bot.add_cog(Fun(bot))