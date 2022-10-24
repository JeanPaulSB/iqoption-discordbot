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