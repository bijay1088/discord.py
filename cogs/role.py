import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

class role(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command(pass_context=True)
  @commands.has_role('admin')
  async def giverole(self, ctx, user: discord.Member, role: discord.Role):
      await user.add_roles(role)
      await ctx.send(f"hey {ctx.author.name}, {user.name} received the role {role.name}")

  @commands.command(pass_context=True)
  @commands.has_role('admin')
  async def removerole(self, ctx, user: discord.Member, role: discord.Role):
      await user.remove_roles(role)
      await ctx.send(f"hey {ctx.author.name}, {user.name} got their {role.name} yeeted.")

  @commands.command()
  async def role(self, ctx, role:discord.Role):
    temp = ["red", "yellow", "orange","green", "blue", "black","purple","white","lavender"]
    user = ctx.message.author
    if role.name in temp:
      for i in range(len(temp)):
        a = discord.utils.get(ctx.guild.roles, name=temp[i])
        await user.remove_roles(a) 
        #await user.remove_roles(a)

      await user.add_roles(role)
      await ctx.send(f"{user} received {role.name}")

    else:
      await ctx.send(f"{user}, you don't have permission to get {role.name}")
      await ctx.send("Available roles are: ")
      await ctx.send(temp)



def setup(client):
  client.add_cog(role(client))