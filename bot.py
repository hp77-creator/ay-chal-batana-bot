#bot.py
import os


from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!ay-chal-batana ')




@bot.command(name='role')
async def tell_role(ctx):
    role = []
    role_li = ctx.author.roles 
    response= ''
    for rol in role_li:
        role.append(rol.name)
    for r in role:
        if r == '@everyone':
            pass
        else:
            response=response+'You have role of '+r+' \n'
    await ctx.send(response)


@bot.command(name='naya role')
async def assign_role(ctx, *, arg):
    member = ctx.message.author
    role = get(member.server.roles, name=arg)
    await bot.add_roles(member, role)

    

bot.run(TOKEN)


