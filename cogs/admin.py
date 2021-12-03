import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

class admin(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Admin is online.')

  #kick
  @commands.command()
  @commands.has_any_role(794521561754238986, 886543778385649724,"admin")
  async def kick(self, ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'Kicked {member}')

  #ban
  @commands.command()
  @commands.has_any_role(794521561754238986, 886543778385649724,"admin")
  async def ban(self, ctx, member: discord.Member, *, reason = None):
    await ctx.send(f'Banned {member}')
    await member.ban(reason = reason)

  #unban
  @commands.command()
  @commands.has_any_role(794521561754238986, 886543778385649724,"admin")
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
      if(user.name,user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
        return
  #clear
  @commands.command()
  @commands.has_any_role('janitor','admin')
  async def clear(self, ctx, amount = 10):
    await ctx.channel.purge(limit = amount+1)

  @commands.command()
  async def info(self, ctx):
    embed = discord.Embed(
      title="About Me", 
      description="I was made by bijay1088#3674.\nI can only do basic functions since Bijay sucks at coding.If you want to invite me to your server, you can use b/invite for link. I don't know why you will do that though, since there is not much I can do.",
      color = 0x2c2f33)
    await ctx.channel.send(embed=embed)


def setup(client):
  client.add_cog(admin(client))