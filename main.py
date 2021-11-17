import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import secreto

token = secreto.seu_token()

intents = discord.Intents.default()
intents.members = True

cb = commands.Bot(command_prefix = "rd!", case_insensitive = True, intents = intents)

@cb.command()
async def rdhelp(ctx):
	embed=discord.Embed(title="Help:",
	                                           description="1 - ip")
	await ctx.send(embed=embed)
@cb.command()
async def ip(ctx):
	embed=discord.Embed(title="IP:",
	                                        description="jogar.redesup.xyz")
	await ctx.send(embed=embed)





@cb.command()
async def enquete(ctx):
	embed=discord.Embed(title="Enquete",
	description=message)
	eqt=cb.get_channel(id=906898533611880488)
	await eqt.send(embed=embed)

@cb.command()
async def nick(ctx, message):
	await ctx.send(f'Quase la {message}!!!')
	rtc=cb.get_channel(id=910327293312925746)
	await rtc.send(f'Nick: {message}')

@cb.command()
async def createchannel(ctx, *, name):
	guild=ctx.guild
	await guild.create_role(name=name)
	await ctx.sebd(f'Cargi {name}')

@cb.command()
async def darcargo(ctx):
	role=discord.utils.get(cb.get_guild(ctx.guild.id).roles, id="906673191521493095")
	guild=ctx.guild
	await guild.add_role(role)





cb.run(token)