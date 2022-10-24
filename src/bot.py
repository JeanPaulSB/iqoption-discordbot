import util
import logging
import discord
import requests



from datetime import datetime, timezone
from discord.ext import commands,tasks

token = 'MTAyOTQ3OTQ0Njc4NjM1OTMyNw.GLqqYk.i157MSMWA5Vb_cNCtvq6Xb9byi9NCmbhf0tZkA'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents = intents)

Agent = util.Agent('','')

"""
TODO: 
- Add emojis to unsuccesfully login and embed message
- implement martin gala 
- let users define its timestamp
"""

@bot.event
async def on_ready():
    print("Bot running...")
    

# bot commands section
@bot.command()
async def register(ctx,*args):
    user = args[0]
    password = args[1]
    email = args[2]
    token = args[3]
    client_id = ctx.message.author.id

    data = {
        'username':user,
        'password':password,
        'clientid':client_id,
        'iqemail': email,
        'token': token
    }

    response = requests.post('http://127.0.0.1:5000/register', json = data)

    print(response.json())

async def loginapi(ctx,*args):
    user  = args[0]
    password = args[1]
    email = args[2]

    data = {
        'username': username,
        'password':password,
        'iqemail':email
    }

    response = requests.post('http://127.0.0.1:5000/register',json = data)
@bot.command()
async def log(ctx,*args):
    user = args[0]
    password = args[1]
    Agent.setUser(user)
    Agent.setPassword(password)
    result = Agent.connect()

    color = discord.Color.green() if result else discord.Color.red()

    if result:
        embedVar = discord.Embed(title = "✅ SUCCESFULLY LOGGED INTO ✅", description="", color = color)
        await ctx.send(embed = embedVar)
    else:
        embedVar = discord.Embed(title = "⛔ THERE WAS AN ERROR, PLEASE CHECK YOUR CREDENTIALS ⛔", description="", color = color)
        await ctx.send(embed = embedVar)        

@bot.command()
async def signal(ctx,*args):
    if Agent.logged:
        user = ctx.message.author.id
        signal = util.Signal(int(args[0]),args[1],args[2],user,int(args[3]))
        
        result = signal.buyNow(Agent.connection)

        await util.printLastPosition(result, ctx, signal,Agent)

    else:
        await ctx.send("You must be logged before taking a signal!")

@bot.command()
async def checkMode(ctx):
    if Agent.logged:
        await ctx.send(f"Your current account mode is -> {Agent.checkMode()}")
    else:
        await ctx.send(f"You are not logged!")

@bot.command()
async def practice(ctx):
    if Agent.logged:
        if Agent.checkMode() == "PRACTICE":
            await ctx.send(f"Your account mode is already PRACTICE!")
        else:
            Agent.setPracticeMode()
            await ctx.send(f"Account mode sucessfully set to -> PRACTICE")
    else:
        await ctx.send(f"You are not logged!")
@bot.command()
async def real(ctx):
    if Agent.logged:
        if Agent.checkMode() == "REAL":
            await ctx.send(f"Your account mode is already REAL!")
        else:
            Agent.setRealMode()
            await ctx.send(f"Account mode sucessfully set to -> REAL")
    else:
        await ctx.send(f"You are not logged!")
@bot.command()
async def balance(ctx):
    if Agent.logged:
        await ctx.send(f"Your balance is -> {Agent.getBalance()}")
@bot.command()
async def getclosed(ctx):
    if Agent.logged:
        closed_positions = Agent.getClosedPositions()
        for position in closed_positions:
            await util.printClosedPosition(ctx, position)

@bot.command()
async def getopen(ctx):
    if Agent.logged:
        
        open_positions = False if len(Agent.getOpenPositions())== 0 else Agent.getOpenPositions()

        if open_positions:
            for position in open_positions:
               await util.printOpenPosition(ctx, position)
        else:
            await ctx.send("⚠️ You have no opened positions until now! ⚠️")

@bot.command()
async def schedulesignal(ctx,*args):
    # same as signal but it has and additional timestamp

    # signal needs the following parameters: money, active,put/call,time,timestamp in hh:mm
    if Agent.logged:
        user = ctx.message.author.id
        signal = util.Signal(int(args[0]),args[1],args[2],user,int(args[3]),args[4])
        signal.scheduled = True
        signal.planned_to_exc = args[4]
        Agent.scheduleSignal(signal)
        
        # setting loop to true and then starting the loop with the task
        await util.printScheduledSignal(ctx, Agent, signal)



        
        
        if not Agent.looping:
            loopingSchedules.start(ctx)
        Agent.looping = True
        
    pass

@bot.command()
async def getscheduleds(ctx):
    if Agent.logged:
        scheduled_signals = Agent.getScheduledSignals()

        if scheduled_signals:
            for signal in scheduled_signals:
                await util.printScheduledSignal(ctx, Agent, signal)
        else:
            await ctx.send("There aro no scheduleds signals")

# function for checking the scheduleds signals in the array and seeing if it's the correct datetime
@tasks.loop(seconds = 5)
async def loopingSchedules(ctx):
    
    now = datetime.now().strftime("%H:%M").split(":")
    hour = now[0]
    minutes = now[1]


    signals = Agent.getScheduledSignals()
    if signals:
        for signal in signals:
            if signal.getPlannedExecution()[0] == hour and signal.getPlannedExecution()[1] == minutes:
                
               
                result = signal.buyNow(Agent.connection)
                Agent.scheduled_signals.remove(signal)
                await util.printLastPosition(result, ctx, signal,Agent)

    else:
        Agent.looping = False
        loopingSchedules.stop()

@bot.command()
async def now(ctx):
    now = datetime.now()
    await ctx.send(now)

bot.run(token)