import os
import discord
import requests
import random
from keepalive import keep_alive
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
import io
import aiohttp
import json
from discord.ext import tasks



client = commands.Bot(command_prefix = 'b/', help_command=None)

bijay = ["bj", "bijay"]

thanks =["thanks bot","thank you bot"]

sad = ["i am sad", "depressed" , "unhappy"]

sorry = ["sorry bot"]

hey = ["hi bot","hey bot","hello bot"]

sucks=['this suck', 'this sucks']

howru=['I am fine.Thanks for asking.','I am not fine right now. Thanks for asking.']

okay=["how are you bot","are you okay bot"]

sad_reply = ["Hang in there ( ͡❛ ⏥ ͡❛)",
"Cheer up ( ͡◡ ‿ ͡◡)",
"Life is better when you’re laughing. ( ͡◡ ͜ʖ ͡◡)",
"You are awesome! Never forget that. ( ͡~ ͜ʖ ͡°)",
"Beautiful. Definition: A person who is reading this. ( ͡~ ͜ʖ ͡°)"]

shut=["shut up bot", "shutup bot", "bot shutup", "bot shut up", "bot suck", "bot useless", "bot is useless", "useless bot"]

task = False

p=True

evoke = "none"

#send stuff in channel
@client.command()
async def send(ctx,channel: discord.TextChannel,*,mes=None):
  global evoke
  if str(ctx.author.id)==evoke:
    await ctx.send("No")
  else:
    await channel.send(mes)
    await ctx.send("Successful.")

#stop send command
@commands.is_owner()
@client.command()
async def evoke_send(ctx,member:discord.Member,y="remove"):
  global evoke
  if y!="remove":
    evoke = str(member.id)
    await ctx.send(f"{member.name} can no longer user send command.")
  else:
    evoke="none"
    await ctx.send(f"{member.name} is free. Have fun :)")
    
#ping me
@commands.is_owner()
@client.command()
async def pingme(ctx):
  global p
  if p:
    p=False
    await ctx.send("You will no longer get ping sire.")
  else:
    p=True
    await ctx.send("You will start to get ping sire.")

#loop a word
@client.command()
@commands.is_owner()
async def loop(ctx):
  global task
  if task:
    mytask.stop()
    await ctx.send("Stopped successful.")
    task=False
  else:
    mytask.start()
    await ctx.send("Started Successful.")
    task=True

@commands.is_owner()
@tasks.loop(seconds=10)
async def mytask():
  channel = client.get_channel(896994767588716564)
  await channel.send("Testing")


  

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} loaded successfully.')
  
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} unloaded successfully.')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


#status
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Streaming(name="Don't click my Stream", url=f"https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
  print('Logged in successfully')

#ping
@client.command()
async def ping(ctx):
  await ctx.send(f'{round(client.latency * 1000)}ms')
  pong = int(f'{round(client.latency * 1000)}') 

  if pong > 50:
    await ctx.send("Sorry, I am kinda slow right now.")
  else:
    return


#dm
@client.command()
async def dm(ctx, user: discord.Member=None,*,message = None):
  embed = discord.Embed(description=message,color=0xFF5733)
  await user.send(embed=embed)

#shut down 
@client.command()
@commands.is_owner()
async def shutdown(ctx):
  await ctx.send("Shutting down.....")
  await ctx.bot.logout()

#help
@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author

  embed = discord.Embed(title="Basic commands",description='invite\ndoggo, catto, fox, meme\npoll title options\ntriggred user\nmath [expression]\nsend [channel] [message]', colour = discord.Color.red())
  embed.add_field(name="Warframe", value="waybound, waybounds, mirage, sister, kavat, syndicate, polarity, baro, simaris, efficiency, trade, quest, crash, \nriven [number_of_positive_stat], riven_help, farm resource_name,\nfusion [highest_percentage]\ncrit [weapon_type] [base_critical_chance]\nkurel",inline=False)
  embed.add_field(name="Games", value="rock, paper, scissors, coin", inline=False)
  embed.set_footer(text='These are help commands.')
  await ctx.send(embed=embed)


#ping me
@client.command(aliases = ['bijay', 'ping_bijay'])
async def _bijay(ctx):
  await ctx.send("<@" + str(563257720321474580) + ">")

#math command
@client.command()
async def math(ctx,*,a:str):
  if set(a).difference(set("1234567890/*-+().")):
    await ctx.send("Math expressions only. :)")
  else:
    ans=eval(a)
    await ctx.send(ans)
    
#invite link
@client.command()
async def invite(ctx):
  await ctx.send("***Do this before invite***: DM Bijay and tell him you are adding me so he can remove some stuff\nHere is your invite link: https://discord.com/api/oauth2/authorize?client_id=896971143800582154&permissions=534150380663&scope=bot")

#coin
@client.command()
async def coin(ctx):
  c = ["head","tail"]
  await ctx.send(random.choice(c))

#command permission error
@client.event
async def on_command_error(ctx, error):
  print(ctx.command.name + " was invoked incorrectly.")
  await ctx.send(error)
  #await ctx.send("<@" + str(563257720321474580) + ">"+" Yoo, I think something is wrong.")

#triggered
@client.command()
async def triggered(ctx, member: discord.Member=None):
  if not member: # if no member is mentioned
    member = ctx.author # the user who ran the command will be the member
        
  async with aiohttp.ClientSession() as trigSession:
    async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg: # get users avatar as png with 1024 size
      imageData = io.BytesIO(await trigImg.read()) # read the image/bytes
            
      await trigSession.close() # closing the session and;
            
      await ctx.reply(file=discord.File(imageData, 'triggered.gif')) # sending the file

#new

bad =["fuck"]

#message line
@client.event
async def on_message(message):
  msg = message.content.lower()

  if any(word in msg for word in thanks):
    await message.channel.send('You are welcome :)') 

  if any(word in msg for word in sad):
    await message.channel.send(random.choice(sad_reply))

  if any(word in msg for word in bad):
    await message.channel.send("Don't be rude :(")

  if any(word in msg for word in sorry):
    await message.channel.send("It's okay ( ᵔ ͜ʖ ᵔ )")

  await client.process_commands(message)

  if message.author == client.user:
        return

  if any(word in msg for word in bijay):
    global p
    if p==True:
      await message.channel.send("<@" + str(563257720321474580) + ">"+" someone wants to talk with you, I think.")

  if any(word in msg for word in hey):
    await message.channel.send("Hi ( ͡ᵔ ͜ʖ ͡ᵔ)")

  if 'give me hug' in msg:
    await message.channel.send("(っ◔◡◔)っ ❤")

  if 'you are best bot' in msg:
    await message.channel.send("No You ☜(ˆ▿ˆc)")

  if any(word in msg for word in shut):
    for i in client.guilds:
      emoji = discord.utils.get(i.emojis, name = "speechless")
    await message.channel.send(emoji)

  if any(word in msg for word in okay):
    await message.channel.send(random.choice(howru))
  
  if any(word in msg for word in sucks):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animu/pat')
      json=await request.json()
    embed=discord.Embed(title= 'Aww', colour=0xFF69B4)
    embed.set_image(url=json['link'])
    await message.reply(embed=embed)

'''
  if 'db' in msg:
    mydb = cluster["discord"]
    mycol = mydb["warframe"]
    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)
    await message.channel.send("successful")'''



  
  



keep_alive()

my_secret = os.environ['token']
client.run(my_secret)

