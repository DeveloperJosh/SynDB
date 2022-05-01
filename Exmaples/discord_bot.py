import discord
from discord.ext import commands
import syndb

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
db = syndb.load("test.db", False)

@bot.command()
async def set_channel(ctx):
    db.set(f"{ctx.guild.id}", ctx.channel.id)
    await ctx.send("Channel Set")
    db.dump()

@bot.command()
async def get_channel(ctx):
    await ctx.send(db.get(f"{ctx.guild.id}"))
    channel = bot.get_channel(db.get(f"{ctx.guild.id}"))
    await channel.send("test")

@bot.command()
async def reset_channel(ctx):
    db.delete(ctx.guild.id)
    await ctx.send("Channel Reset")

bot.run("Your Token")