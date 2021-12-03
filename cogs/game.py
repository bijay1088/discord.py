import discord
import random
from discord.ext import commands

spr = ["paper", "rock", "scissor"]
class game(commands.Cog):

  def __init__(self, client):
    self.client = client

  #paper rock scissor
  @commands.command(aliases=["rock paper", "paper rock", "paper rock scissors", "rock paper scissors","rock", "paper", "scissor"])
  async def _rock(self, ctx):
    while True:
      a=1
      check = lambda m: m.author == ctx.author and m.channel == ctx.channel
      await ctx.send("Rock Paper....")
      bot=random.choice(spr)
      temp= await self.client.wait_for('message', check=check)
      temp=temp.content.lower()
      #paper
      if(temp=="paper"):
        await ctx.send(bot)
        if(bot=="scissor"):
          await ctx.send("I win. :)")
        elif(bot=="paper"):
          await ctx.send("Oof")
        else:
          await ctx.send("You win. :(")
      #scissor
      elif(temp=="scissor"):
        await ctx.send(bot)
        if(bot=="rock"):
          await ctx.send("I win. :)")
        elif(bot=="scissor"):
          await ctx.send("Oof")
        else:
          await ctx.send("You win. :(")
      #rock
      elif(temp=="rock"):
        await ctx.send(bot)
        if(bot=="paper"):
          await ctx.send("I win. :)")
        elif(bot=="rock"):
          await ctx.send("Oof")
        else:
          await ctx.send("You win. :(")
      #if wrong word 
      else:
        await ctx.send("Type 'rock' or 'paper' or  'scissor' after I say Rock Paper....")
      if a == 1:
        await ctx.send("Do you still wanna play? (Y/N)")
        b= await self.client.wait_for('message',check=check)
        b=b.content.lower()
        if(b!='y'):
          await ctx.send("Bye :(")
          return


def setup(client):
  client.add_cog(game(client))