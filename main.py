import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=">",
                      case_insensitive=True,
                      intents=intents)

@client.event
async def on_ready():
	print('entramos como {0.user}'.format(client))


@client.command()
async def ola(ctx):
	await ctx.send(f'Eu sou Lindoh, {ctx.author}')


@client.command()
async def dado(ctx, numero):
	variavel = random.randint(1, int(numero))
	await ctx.send(f'O número que saiu no dado é {variavel}')


@client.command()
async def on_member_join(member):
	canalboasvindas = client.get_channel(873753031924121620)
	regras = client.get_channel(873757514485858304)
	sejastaff = client.get_channel(873817275839438868)
	registrese = client.get_channel(874119520707555368)

	mensagem = await canalboasvindas.send(
	    f"**Bem vindo ao Imperio Celestial** {member.mention} **Leia as**  {regras.mention} **e** {sejastaff.mention} **Registre-se Aqui** {registrese.mention}"
	)

	await asyncio.sleep(20)

	await mensagem.delete()


client.run('token do bot')
