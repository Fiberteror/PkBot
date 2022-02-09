import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ";", case_insensitive = True)
@client.event
async def on_ready():
  print('Entramos como {0.user}' .format(client))

arquivo = open("current_updates.txt")
lines = []
with open('current_updates.txt') as f:
    for line in f:
        lines.append(line)

@client.command(aliases=['ajuda'])
async def helpp(ctx):
  await ctx.author.create_dm()
  await ctx.author.dm_channel.send(
    embed = discord.Embed(
      title = "**Commands:**",
      description = "Calc-(;Calc (Number) (+,-,*,/) (Number))\n Icon-;Icon(@Member)\n dado-;dado (Number)\n dm-;dm (Message) (@Member)\n fale-;fale (Message)\n id-;id (Member)\n dme-;dme (Message)\n embed-;embed (Titulo/title)(Descrição/Description)[com as aspas]\n cores/colours/colors-;cores (Mostra o código das cores para sua embed./Show the colours code for your embed.)",
      colour = 16711680
     )
  )

  await ctx.send('Informações enviadas por DM! :incoming_envelope: ')

@client.command()
async def dme(ctx, arg):
  await ctx.author.create_dm()
  await ctx.author.dm_channel.send(arg)

@client.command()
async def dm(ctx, arg, user_mentioned: discord.Member):
  await user_mentioned.create_dm()
  await user_mentioned.dm_channel.send(arg)
  await ctx.message.delete()

@client.command(aliases=['desafiar'])
async def apostar(ctx,money:int,moeda,mention:discord.Member):
  channel1 = client.get_channel(939960137454600223)
  msg = await ctx.send(f"{ctx.author} está desafiando {mention} por {money} {moeda}. Para {mention} aceitar a aposta, reaja abaixo, para rejeitar, apenas não faça nada.")
  yas = '✔️'
  await msg.add_reaction(yas)
  def check(reaction, user):
        return user == mention and str(reaction.emoji) == '✔️'
  await client.wait_for('reaction_add', timeout=60.0, check=check)
  embed = discord.Embed(
    title='Aposta',
    description=f'{ctx.author} desafiou {mention} em uma Batalha PokéTwo por {money} {moeda}.'
  )
  embed.set_thumbnail(
            url=f"{ctx.author.avatar_url}"
        )
  await channel1.send(embed=embed)
  await msg.remove()

@client.command()
async def open_ip(ctx, channelid: int):
    role = discord.utils.get(Role, name="Membros")
    await ctx.channelid.set_permissions(role, send_messages=False)
    await ctx.send("Configurações atualizadas com sucesso.")

@client.command()
async def id(ctx, user_mentioned: discord.Member):
  await ctx.reply(user_mentioned.id)

@client.command()
async def embed(ctx,arg1,arg2, n: int):
  embed = discord.Embed(
    title = (arg1),
    description = (arg2),
    colour = n
  )
  await ctx.send(embed = embed)
  await ctx.message.delete()

@client.command(aliases=['colours', 'colors'])
async def cores(ctx):
  embed = discord.Embed(
  title = "Cores/Colours",
  description = 'Red/Vermelho = 16711680\n Green/Verde = 32768\n Yellow/Amarelo = 16766720\n Blue/Azul = 255 \n White/Branco = 16777215\n Gray/Cinza = 8421504\n Pink/Rosa = 16761035\n Black/Preto = 0\n Orange/Laranja = 16753920\n Brown/Marrom = 10824234'
  )
  await ctx.send(embed = embed)

@client.command()
async def Olá(ctx):
 await ctx.send(f'Olá, como você está?{ctx.author}')

@client.command(aliases=['Atualizacao', 'Atualizacoes', 'upt'])
async def Updates(ctx):
  global lines
  embed = discord.Embed(
    title = f"{lines[0]}",
    description = f"{lines[1]}"
  )
  embed.add_field(name=f"{lines[2]}", value=f"{lines[3]}", inline=False)
  embed.add_field(name=f"{lines[4]}", value=f"{lines[5]}", inline=False)
  await ctx.send(embed = embed)

@client.command()
async def fale(ctx, arg):
  await ctx.send(arg)
  await ctx.message.delete()

@client.command()
async def Icon(ctx, user_mentioned: discord.Member):
  icon_url = user_mentioned.avatar_url
  await ctx.reply(f'{icon_url}')

@client.command()
async def on(ctx):
  await ctx.send(f'Estou aqui!')

@client.command(aliases=['caucule', 'calcular'])
async def Calc(ctx,a:int,arg,b:int):
 if arg == '+':
   await ctx.send(f"{a} + {b} = {a+b}")
 if arg == '-':
   await ctx.send(f"{a} - {b} = {a-b}")
 if arg == '*':
   await ctx.send(f"{a} * {b} = {a*b}")
 if arg == '/':
   await ctx.send(f"{a} / {b} = {a/b} e o resto é: {a%b}")
 if arg == '÷':
   await ctx.send(f"{a} ÷ {b} = {a/b} e o resto é: {a%b}")
 if arg == ':':
   await ctx.send(f"{a} : {b} = {a/b} e o resto é: {a%b}")

@client.command()
async def dado(ctx, numero):
 variavel = random.randint(1,int(numero))
 await ctx.send(f'O número que saiu é:{variavel}')

client.run('OTI2MjA3ODc0MDQzMDk3MTk5.Yc4UTQ.LZWoKCU4w8gwCTK4dqSl3tALH9k')
