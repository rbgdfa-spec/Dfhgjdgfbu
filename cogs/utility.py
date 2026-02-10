import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Here are the available commands...")

    @commands.command()
    async def botinfo(self, ctx):
        await ctx.send(f"Bot Name: {self.bot.user.name}\nBot ID: {self.bot.user.id}")

    @commands.command()
    async def serverinfo(self, ctx):
        server = ctx.guild
        await ctx.send(f"Server Name: {server.name}\nServer ID: {server.id}")

    @commands.command()
    async def prefix(self, ctx):
        await ctx.send(f"My prefix is: {self.bot.command_prefix}")

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("[Invite Link](https://discordapp.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot)")

    @commands.command()
    async def changelog(self, ctx):
        await ctx.send("Changelog: ...")

def setup(bot):
    bot.add_cog(Utility(bot))