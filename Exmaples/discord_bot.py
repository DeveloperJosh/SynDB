import discord
from discord.ext import commands
import syndb

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
db = syndb.load("test.db", False)

@bot.command()
async def set_channel(ctx):
    db.set(ctx.guild.id, ctx.channel.id)
    await ctx.send("Channel Set")
    db.dump()

@bot.command()
async def get_channel(ctx):
    await ctx.send(db.get(ctx.guild.id))

@bot.command()
async def reset_channel(ctx):
    db.delete(ctx.guild.id)
    await ctx.send("Channel Reset")

bot.run(f"your_token_here")