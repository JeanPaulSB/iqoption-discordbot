import util
import discord
from datetime import datetime

# miscellanous functions for sending embed messages

async def printLastPosition(result,ctx,signal,Agent):
    color = discord.Color.green() if result else discord.Color.red()

    direction_emoji = ' 📈' if signal.direction == "call" else ' 📉' 

    signal.direction += direction_emoji 

    if result:
           
        position = Agent.getOpenPositions()[-1]

        created = datetime.fromtimestamp(position['created']).strftime('%Y-%m-%d %H:%M:%S')
        expired = datetime.fromtimestamp(position['expired']).strftime('%Y-%m-%d %H:%M:%S')

        embedVar = discord.Embed(title = "💰 Action sucessfully bought! 💰", description="",color = color)
        embedVar.add_field(name = "Active", value = position['active'],inline = True)
        embedVar.add_field(name = "Created at",value = created,inline = True)
        embedVar.add_field(name = "Expired at",value = expired,inline = True)
        embedVar.add_field(name = "Sum", value = position['sum'],inline = True)
        embedVar.add_field(name = "Direction", value = signal.direction, inline = True)
        embedVar.add_field(name = "Win amount", value = position['win_amount'],inline = True)

        await ctx.send(embed = embedVar)
            
    else:
        embedVar = discord.Embed(title = "⛔ Hmmm, something went wrong ⛔", description="",color = color)
        await ctx.send(embed = embedVar)


async def printScheduledSignal(ctx,Agent,signal):
            embedVar = discord.Embed(title = "🏁 SCHEDULED SIGNAL 🏁", description="",color = discord.Color.blue())
            embedVar.add_field(name = "Active", value = signal.actives ,inline = True)
            embedVar.add_field(name = "Created at",value = signal.created_at,inline = True)
            embedVar.add_field(name = "Sum", value = signal.money ,inline = True)
            embedVar.add_field(name = "Plan to be executed at: ", value = signal.planned_to_exc,inline = True)
            await ctx.send(embed = embedVar)

async def printscheduleSignal(ctx,Agent,signal):
    embedVar = discord.Embed(title = "🏁 SCHEDULED SIGNAL 🏁", description="",color = discord.Color.blue())
    embedVar.add_field(name = "Active", value = signal.actives ,inline = True)
    embedVar.add_field(name = "Created at",value = signal.created_at,inline = True)
    embedVar.add_field(name = "Sum", value = signal.money ,inline = True)
    embedVar.add_field(name = "Plan to be executed at: ", value = signal.planned_to_exc,inline = True)
    await ctx.send(embed = embedVar)

async def printOpenPosition(ctx,position):
        created = datetime.fromtimestamp(position['created']).strftime('%Y-%m-%d %H:%M:%S')
        expired = datetime.fromtimestamp(position['expired']).strftime('%Y-%m-%d %H:%M:%S')

        embedVar = discord.Embed(title = "🏁 OPENED POSITION 🏁", description="",color = discord.Color.blue())
        embedVar.add_field(name = "Active", value = position['active'],inline = True)
        embedVar.add_field(name = "Created at",value = created,inline = True)
        embedVar.add_field(name = "Expired at",value = expired,inline = True)
        embedVar.add_field(name = "Sum", value = position['sum'],inline = True)
        embedVar.add_field(name = "Win amount", value = position['win_amount'],inline = True)
                

        await ctx.send(embed = embedVar)

async def printClosedPosition(ctx,position):
        created = datetime.fromtimestamp(position['created']).strftime('%Y-%m-%d %H:%M:%S')
        expired = datetime.fromtimestamp(position['expired']).strftime('%Y-%m-%d %H:%M:%S')

        color = discord.Color.green() if position['win'] == 'win' else discord.Color.red()
            
        emoji = '✅' if position['win'] == 'win' else '❌'
            

        embedVar = discord.Embed(title = position['active'] + emoji, description="",color = color)
        embedVar.add_field(name = "Created at",value = created,inline = True)
        embedVar.add_field(name = "Expired at",value = expired,inline = True)
        embedVar.add_field(name = "Amount", value = position['amount'],inline = True)
        embedVar.add_field(name = "Win amount", value = position['win_amount'],inline = True)
            

        await ctx.send(embed = embedVar)

async def printBalance(ctx,amount):
    color = discord.Color.yellow()
    embedVar = discord.Embed(title = "💳 BALANCE 💳", description= "Your balance in the current account mode", color = color)
    embedVar.add_field(name = "Amount", value =f"💵 {amount} 💵")
    await ctx.send(embed = embedVar)

async def printLoginRequired(ctx):
    color = discord.Color.red()
    embedVar = discord.Embed(title = "🕵🏿‍♀️ You are not logged 🕵🏿‍♀️",description = "Please login before executing any commmand",color = color)
    await ctx.send(embed =  embedVar)

async def printZeroScheduledSignals(ctx):
    color = discord.Color.red()
    embedVar = discord.Embed(title = "⛔ You don't have scheduled signals! ⛔",description = "You don't have any scheduled signal at this point, try scheduling a new one!", color = color)
    await ctx.send(embed = embedVar)


####
async def printMartinGalaStatus(ctx,Agent):

    status = Agent.checkMartinGala()

    color = discord.Color.green() if status else discord.Color.red() 
    message = "⛔ Martin Gala is already ON! ⛔" if status else "⛔ Martin Gala is already OFF! ⛔"

    embedVar = discord.Embed(title = message, description = "", color = color)
    await ctx.send(embed = embedVar)

async def printMartinGalaON(ctx):
    color = discord.Color.green()
    embedVar = discord.Embed(title = "🚦 Martin Gala turned ON 🚦 ", description = "⚠️ Martin gala is ON, be carefully to turn it OFF again if needed ⚠️")
    await ctx.send(embed = embedVar)

async def printMartinGalaOFF(ctx):
    color = discord.Color.green()
    embedVar = discord.Embed(title = "🚧 Martin Gala turned OFF 🚧 ", description = "⚠️ Martin gala is OFF, be carefully to turn it ON again if needed ⚠️")
    await ctx.send(embed = embedVar)
async def printMartinGala(ctx,Agent):

    status = Agent.checkMartinGala()
    color = discord.Color.green() if status else discord.Color.red() 
    emoji = '🚀' if status else '🚨'
    message = "Martin gala is ON" if status else "Martin gala is OFF"


    embedVar = discord.Embed( title = "🛑 Martin Gala current status 🛑 ", description = f"{emoji} {message} {emoji}")
    await ctx.send(embed = embedVar)



async def printClock(ctx,now):
    color = discord.Color.blue()
    embedVar = discord.Embed(title = "⏲️ Current time (GMT -5:00) ⏲️",description= f"{now}")
    await ctx.send(embed = embedVar)