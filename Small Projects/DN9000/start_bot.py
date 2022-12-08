import discord
import pandas as pd
import DN9000_Key

DNKey = DN9000_Key.D_Key
client = discord.Client()

@client.event
async def on_ready(): #When bot is ready to be used, lets it be known in the console
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$Hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$Spam"):
        for i in range(0,10):
            await message.channel.send("Spamming!")

            
    


    print()
    print(message)

client.run(DNKey)

