import discord
from discord.ext import commands
import json


class warframe(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Warframe is online.')


  #https://warframe.fandom.com/api.php?action=query&list=search&srsearch=%7Bsearch



  #farm 
  @commands.has_role('farmer')
  @commands.command()
  async def add_farm(self,ctx):
    filename="farm.json"
    check = lambda m: m.author == ctx.author and m.channel == ctx.channel
    test=["resource","location","planet"]
    a=0
    for i in test:
      await ctx.send("Enter the "+i)
      temp= await self.client.wait_for('message', check=check)
      if temp.content.lower()=="cancel":
        await ctx.send("Stopped.")
        return
      else:
        test[a]=temp.content.upper()
        a=a+1
    if temp.content.lower()!="cancel":
      with open(filename, "r") as file:
        data = json.load(file)
        y = {
          test[0]:{
            "location": test[1],
            "planet": test[2] 
            }
          }
        data.update(y)

    with open(filename, "w") as f:
      json.dump(data, f, indent=4)

    await ctx.send(test[0]+" has been successfully added.")

  @commands.command()
  async def farm(self, ctx,*,words):
    resource = words.upper()

    with open("farm.json") as f:
      data = json.load(f)
      try:
        
        await ctx.send("Node Name: "+data[resource]["location"]+"\nPlanet: "+data[resource]["planet"])
      except  KeyError:
        await ctx.send("That resource is not added yet.")
      
       



  #valence
  @commands.command()
  async def fusion(self, ctx, *, message:float):
    try:
      if message<=60 and message>=25:
        message = message*1.1
        if message>=60:
          message=60
        await ctx.send("Your % after fusion is "+str(message)+"%")
      else:
        await ctx.send("Enter valid number.")
    except:
      await ctx.send("Enter valid number.")

    
  #kavat
  @commands.command() 
  async def kavat(self, ctx):
    await ctx.send('craft a kavat incubator upgrade segment, blueprint in dojo or you can also get it from hyekka masters(1.5% chance)\nthen equip a scanner and go to Deimos non open world (recommended: Capture) and scan kavats (25% chance)\nafter u get 10 codes by scanning, u can do random incubation to get either adarza or smeeta, both have same chance\nif you want a specific kavat, you can use imprints which u can get from other players by trading\nif you want vasca, you have to let vasca from Plain of eidolon bite your kavat(your kavat will get a ephemera like thingy once it gets the virus) which spawn during night time, then make imprint out of that kavat and use it to make vasca') 

  #sister
  @commands.command()
  async def sister(self, ctx):
    await ctx.send("Make sure you don't have any active lich, finish call of tempestari and deadlock protocol\nGo to Hydra, Pluto\nFind thanos gauntlet\nThere should be console there you can interact, sacrifice Zenith Crown and get inside\nGet 25 kills(use mesa or xoris to make it easy) (solo)\nGet out of void(either by letting timer reach 0 or getting 75 kill)\nDo mission normally but don't speedrun (don't get near extraction too)\nYou will get a transmission from Sister saying they found someone and a unique enemy will be marked in map\nDefeat it and they will fall(There will be a small window above their head showing which weapon they have)\nDefeat them(default option is holding X) to convert them into sister\nAfter you successfully do this, finish mission, you get your sister\n\ns/howto lich 2nd page in #botspam  for more guide on how to murmur\n")

  #mirage
  @commands.command()
  async def mirage(self, ctx):
    await ctx.send('1st part: Olympus, Mars\n2nd part: Calypso, Saturn\n3rd part: Charybdis, Sedna')

  #waybound
  @commands.command(aliases=['waybound' , 'waybounds'])
  async def _waybound(self, ctx):
    await ctx.send('Zenurik:\nVoid Siphon and Flow\n\nMadurai:\nInner and Eternal Gaze\n\nUnairu:\nBasilisk Scales and Gaze\n\nNaramon:\nMind Step and Sprint\n\nVazarin:\nEnduring and Rejuvenating Tides')

  #syndicate
  @commands.command()
  async def syndicate(self, ctx):
    await ctx.send('Link:https://cdn.discordapp.com/attachments/850688617705373716/880815150238691398/unknown.png')

  #polarity
  @commands.command()
  async def polarity(self, ctx):
    await ctx.send('Link:https://cdn.discordapp.com/attachments/850688617705373716/880843275647475712/polarity_LI.jpg')

  #rotation
  @commands.command()
  async def rotation(self,ctx):
    await ctx.send("`**AABC-AABC-.... gang**\n-For Defence and Survival, every 5 min/wave is one rotation\n-Excavation, Interception, Infested salvage is every 1 driller(2 for fissure)/message/manifests\n-Defection is every 2 squad\n-Elite/Sanctuary Onslaught is every 2 zone\n-Orphix is every 3 orphix\n\n**ABC gang**\n-Spy and Cache is every 1 vault/cache (opening 2 vault/cache gives reward from A and B as example)\n-Granum void is every 25 kill (+25 more per player in squad)\n-Rescue, For A. Rescue with only alarm \n                       B. Stealth rescue or Kill all warden\n                       C. All above\n\n**AABBCCCCCCC..........**\n-Arbitration only\n\n**s/essential disruption**\n-Use this in #botspam for disruption\n\n**Bounty**\n-Open world bounty rotate after specific amount of time (you can look at timer above bounty to see when next will show up and use wiki as reference to know which rotation is current)`")

#capacity
  @commands.command()
  async def capacity(self,ctx):
    await ctx.send("Link: https://cdn.discordapp.com/attachments/850688617705373716/880843301706661928/capacity_LI.jpg")
    
    #crash
  @commands.command()
  async def crash(self,ctx):
    await ctx.send("Link: https://cdn.discordapp.com/attachments/850688617705373716/880130830490542150/unknown.png")

#simaris
  @commands.command()
  async def simaris(self,ctx):
    await ctx.send("Link: https://cdn.discordapp.com/attachments/850688617705373716/880123879987769414/Simaris.png")

#baro
  @commands.command()
  async def baro(self,ctx):
    await ctx.send("Link: https://cdn.discordapp.com/attachments/850688617705373716/865590328082038834/baro.png")

#effi
  @commands.command()
  async def efficiency(self,ctx):
    await ctx.send("Link: https://cdn.discordapp.com/attachments/150313159343865856/860062546656493578/641.png")

    #main quest
  @commands.command()
  async def quest(self,ctx):
    await ctx.send("Vor's prize \nOnce awake\nThe archwing \nStolen dreams \nThe new strange \nNatah \nThe second dream\nThe war within \nChains of harrow \nApostasy prologue \nThe sacrifice \nChimera prologue\nErra\nThe Maker")

  #trade
  @commands.command()
  async def trade(self,ctx):
    await ctx.send("You either go to dojo or maroo\nDojo: There is trading post u can use             \nOr, hold gear button and set up shop\nMaroo bazar: use gear function from top")

  #inaros
  @commands.command()
  async def inaros(self,ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/853238767511142400/904393107460751451/unknown-37.png')
    
  #rotation
  @commands.command()
  async def rotation(self,ctx):
    await ctx.send("Not ready yet")

  #kurel
  @commands.command()
  async def kurel(self,ctx,*,message):
    if message == "tracker":
      await ctx.send("Here is your mastery tracker made by kurel: \nhttps://docs.google.com/spreadsheets/d/1GPq7u55Wpez5jICro8EretrB4Zv1LnoG8YjnFVxCTfg/edit#gid=0")

    elif message == "market":
      await ctx.send("Here is kurel guide for warframe.market:\nhttps://cdn.discordapp.com/attachments/850688617705373716/877773295745925141/unknown.png")

    elif message == "affinity":
      await ctx.send("Affinity farms: Adaro stealth run > ESO leech (weapons only) > SO leech > Hydron > Helene")
    
    elif message=="credit":
      await ctx.send("Credit farms: Profit-Taker speedruns > Index high risk > Ceres dark sectors > any earlier dark sectors")

    elif message=="endo":
      await ctx.send("Endo farms: SP Vodyanoi w/ premade > regular Vodyanoi w/ premade > Arbys > Necralisk T5 bounty, first stage > Cetus/Fortuna T5 bounty, first stage > Veil Proxima Void Storms > Void Sabotage caches > Cholistan or Hieracon, rotation A")

    elif message == "kuva":
      await ctx.send("Credits to kurel\nKuvruption calculations use 3 minute rotations. All Kuva numbers after converting VE/SE to Kuva. SP assumes 1 Acolyte spawn per 5 minutes. Arby assumes 50/100 VE per hour. YMMV.\n\nw/ resource booster: Arby Kuvival (56k per hour) > Arby Kuvruption (51k per hour) > SP Kuvival (48k per hour) > SP Kuvruption (47k per hour) > any other Arby (40k per hour) > Kuvival fissure (35.6k per hour) > any other SP mission (32k per hour) > Kuvruption fissure (29k per hour)\n\nw/o resource booster: Arby Kuvruption (29k per hour) > Arby Kuvival (28k per hour) > SP Kuvruption (27k per hour) > SP Kuvival (24k per hour) > any other Arby (20k per hour) > Kuvruption fissure (18k per hour) > Kuvival fissure (17.8k per hour) > any other SP mission (16k per hour)")
    else :
      await ctx.send("Available commands:\ntracker\nmarket\naffinity\nendo\ncredit\nkuva")


def setup(client):
  client.add_cog(warframe(client))