import discord
from discord.ext import commands


class Modmail(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    @commands.dm_only()
    async def on_message(self, message: discord.Message):
        """simple modmail event, it works, that's all that matters."""
        
        if message.author.bot:
            return
        
        else:
            if message.channel == message.author.dm_channel:
  

                self.channel_id = 900008500049092720
                self.modmail_channel = self.bot.get_channel(self.channel_id)
                embed = discord.Embed(
                    title = f"Modmail From `{message.author}`", 
                    description = f"{message.content}", 
                    color = 0x2c2f33
                )
                if message.attachments:
                    embed.set_image(url=message.attachments[0].url)
                embed.set_footer(text=f'ID: {message.author.id}')

                await self.modmail_channel.send(embed=embed)

        

def setup(bot):
    bot.add_cog(Modmail(bot))