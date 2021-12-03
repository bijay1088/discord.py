import discord
from discord.ext import commands
import json


class riven(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command() 
  async def riven(self, ctx,*,message):
    if message == "3":
      check = lambda m: m.author == ctx.author and m.channel == ctx.channel
      riv=['Prefix','Core','Suffix']
      a=0
      for i in riv:
        await ctx.send("Enter the riven name: "+i)
        temp= await self.client.wait_for('message', check=check)
        temp=temp.content.lower()
        riv[a]=temp
        a=a+1
      with open("riven.json") as f:
        data = json.load(f)
      b=0
      await ctx.send("Stats:")
      for i in range(len(riv)-1):
        try:
          stat = data["prefix"][riv[b]]
        except  KeyError:
          stat = "Not found"
        await ctx.send(stat)
        b=b+1
      try:
        stat = data["suffix"][riv[2]]
      except  KeyError:
        stat = "Not found"
      await ctx.send(stat)

    elif message=="2":
      check = lambda m: m.author == ctx.author and m.channel == ctx.channel
      riv=['Prefix','Suffix']
      a=0
      for i in riv:
        await ctx.send("Enter the riven name: "+i)
        temp= await self.client.wait_for('message', check=check)
        temp=temp.content.lower()
        riv[a]=temp
        a=a+1
      with open("riven.json") as f:
        data = json.load(f)
      b=0
      await ctx.send("Stats:")
      for i in range(len(riv)-1):
        try:
          stat = data["prefix"][riv[b]]
        except  KeyError:
          stat = "Not found"
        await ctx.send(stat)
        b=b+1
      try:
        stat = data["suffix"][riv[1]]
      except  KeyError:
        stat = "Not found"
      await ctx.send(stat)
    
    else:
      await ctx.send("Please input either 2 or 3.")

    
    """"
      for i in riv:
      if riv[b] =="laci":
        await ctx.send("Additional Combo Count Chance")
      else:
        await ctx.send("None")
      b=b+1"""


  @commands.command() 
  async def riven_help(self, ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/853238767511142400/904337109974925352/unknown.png")





def setup(client):
  client.add_cog(riven(client))
          
    