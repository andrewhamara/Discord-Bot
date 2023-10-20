import discord
from discord.ext import commands
#from myCommands import MyCommands

# # # # # # # # # # # # # # # # #

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
#bot.add_cog(MyCommands(bot))

with open('token.txt', 'r') as f:
    token = f.read()

# # # # # # # # # # # # # # # # #

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)


def run():

    @bot.event
    async def on_ready():
        print('Logged in as ' + str(bot.user) + '\n********')

    try:
        bot.run(token.strip())
    except Exception as e:
        print('Bot failed: ' + str(e))

if __name__ == "__main__":
    run()
