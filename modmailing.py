import discord
import asyncio
from discord import message
from discord.ext import commands
from discord import Embed

token= "insert token"
bot = commands.Bot(command_prefix=commands.when_mentioned_or("-"), case_insensitive=True)
bot.remove_command("help")
prex="-"

@bot.event
async def on_ready():
    print("Modmail ready for use")
    while True:
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("[-] Modmail >> Dm me for support"))

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
            em = discord.Embed(color=0xAD1457)
            em.add_field(name="**Modmailing**", value=f"User: {message.author.mention} ({message.author})\nUser ID: {message.author.id}\nneeds help with: {message.content}\n\nto reply: -report {message.author.mention} [message]")
            await bot.get_guild(INSERT_GUILD_ID).get_channel(INSERT_CHANNEL_ID).send(embed=em)
        await bot.process_commands(message)

@bot.command(usage=f"{prex}reply [mention]", description="reply to a modmail Dm", brief="main")
async def reply(ctx, member:discord.Member, *, msg):
    await member.send(msg)

@bot.command(usage=f"{prex}help", description="this message", brief="main")
async def help(ctx):
    await ctx.message.delete()
    commandinfo = ''
    for command in bot.commands:
        if command.brief == "main":
         commandinfo += f'{command.usage} | {command.description}\n'
    embed = discord.Embed(title="Modmail", description=f'\n{commandinfo}', color=0xAD1457)
    embed.set_thumbnail(url="")
    embed.set_footer(text="")
    await ctx.send(embed=embed)

bot.run(token)
