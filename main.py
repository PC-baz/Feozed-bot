import discord
from discord.ext import commands 
from discord_slash import SlashCommand

Token = ''

intents = discord.Intents.all()
client = commands.Bot(command_prefix='@', help_command=None, intents=intents)
slash = SlashCommand(client, sync_commands=True)


@slash.slash(name="create_channel", description="create channel", guild_ids=[843694293708963890])
async def create_channel(ctx, channel_name):
	guild = ctx.guild
	channel = await guild.create_text_channel(channel_name)


@client.command()
async def say(ctx, message=None):
    await ctx.send(message)

@client.command()
async def create_channel(ctx, channel_name):
	guild = ctx.guild
	channel = await guild.create_text_channel(channel_name)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def help(ctx):
    help = discord.Embed(title="help command",  colour=0x4472F0)
    help.add_field(name="info", value="@info", inline=False)
    help.add_field(name="link", value="@link", inline=False)
    await ctx.reply(embed=help)

@slash.slash(name="help", description="help command❓")
async def help(ctx):
    help = discord.Embed(title="help command",  colour=0x4472F0)
    help.add_field(name="info", value="@info", inline=False)
    help.add_field(name="link", value="@link", inline=False)
    await ctx.send(embed=help)

@client.command()
async def info(ctx):
    info = discord.Embed(title="info command", colour=0x4472F0)
    info.add_field(name="members:", value=ctx.guild.member_count, inline=False)
    info.add_field(name="server name:", value=ctx.guild.name, inline=False)
    info.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y at %H:%M:%S'), inline=False)
    info.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.reply(embed=info)

@slash.slash(name="info", description="info command📄")
async def info(ctx):
    info = discord.Embed(title="info command", colour=0x4472F0)
    info.add_field(name="members:", value=ctx.guild.member_count, inline=False)
    info.add_field(name="server name:", value=ctx.guild.name, inline=False)
    info.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y at %H:%M:%S'), inline=False)
    info.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=info)

@client.command()
async def link(ctx):
    info = discord.Embed(title="links", colour=0x4472F0)
    info.add_field(name="Aparat:", value="https://www.aparat.com/Darky_DW", inline=False)
    info.add_field(name="youtube:", value="https://www.youtube.com/channel/UCJI3CLnMBZrh5pZblLmPZpg", inline=False)
    info.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.reply(embed=info)

@slash.slash(name="link", description="link 🔗")
async def link(ctx):
    info = discord.Embed(title="links", colour=0x4472F0)
    info.add_field(name="Aparat:", value="https://www.aparat.com/Darky_DW", inline=False)
    info.add_field(name="youtube:", value="https://www.youtube.com/channel/UCJI3CLnMBZrh5pZblLmPZpg", inline=False)
    info.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=info)

@client.event
async def on_ready():
    print('bot is ready')
    await client.change_presence(activity=discord.Game(name="@help | Darky DW"))

client.run(Token)
