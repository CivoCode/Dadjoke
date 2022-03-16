import nextcord
import requests
from aiohttp import request
from nextcord.ext import commands



bot = commands.Bot(command_prefix="!")

@bot.command(name="dadjoke", aliases=["dadjokes", "dj"])
async def dadjoke(ctx):

    url = "https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes"

    async with request("GET", url, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(f"**{data['setup']}**\n\n||{data['punchline']}||")
        else:
            await ctx.send(f"{response.status}")


bot.run("")
