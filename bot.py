import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=';')
bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzQzOTEyODg2MTE5Njk0MzM2.Xzbk3Q.W3rcrOOkHlUeNZsmiFjIsJ5gUuI')