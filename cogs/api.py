import discord
from discord.ext import commands
import aiohttp
import json
from discord import Member
import requests

class api(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Api is online.')


  #doggo
  @commands.command(aliases=['doggos' , 'dog', 'doggo','dogs'])
  async def _dog(self, ctx):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://dog.ceo/api/breeds/image/random')
      dogjson = await request.json()
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

    embed = discord.Embed(title="Doggo!", color=discord.Color.purple())
    embed.set_image(url=dogjson['message'])
    embed.set_footer(text=factjson['fact'])
    await ctx.send(embed=embed)

  #fox
  @commands.command(aliases=['fox','foxes'])
  async def _fox(self, ctx):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/fox')
      foxjson=await request.json()
      request2 = await session.get('https://some-random-api.ml/facts/fox')
      factfox = await request2.json()

    embed = discord.Embed(title="Fox")
    embed.set_image(url=foxjson['link'])
    embed.set_footer(text=factfox['fact'])
    await ctx.send(embed=embed)


  #catto
  @commands.command(aliases=['cattos' , 'cat', 'catto','cats'])
  async def _cat(self, ctx):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animal/cat')
      catjson = await request.json()
    embed = discord.Embed(title="Catto", color =discord.Color.red())
    embed.set_image(url=catjson["image"])
    embed.set_footer(text= catjson["fact"])
    await ctx.send(embed=embed)
    print(catjson)

  #meme
  @commands.command()
  async def meme(self, ctx):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://meme-api.herokuapp.com/gimme')
      memejson = await request.json()
    embed = discord.Embed(title="Source:Reddit", color =discord.Color.red())
    embed.set_image(url=memejson['url'])
    await ctx.send(embed=embed)

  #hug
  @commands.command()
  async def hug(self, ctx):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animu/hug')
      memejson = await request.json()
    await ctx.send(memejson['link'])

  


def setup(client):
  client.add_cog(api(client))