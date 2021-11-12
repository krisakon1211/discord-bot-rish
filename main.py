import typing_extensions
import discord
from discord.ext import commands
from datetime import datetime , timedelta


# wrapper / decorator

message_lastseen = datetime.now()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")



@bot.event
async def on_message(message):
    global message_lastseen
    if message.content == '!newbie' and datetime.now() >= message_lastseen:
        print(message.channel)
        message_lastseen = datetime.now() + timedelta(seconds=10)
        await message.channel.send('https://www.youtube.com/user/bisbkk')
        await message.channel.send('https://www.youtube.com/c/ILearnALotAboutBitcoin')

    elif message.content == '!future':
        await message.channel.send('https://www.youtube.com/watch?v=8qOddyGXRe0')

    elif message.content == '!bitkub':
        await message.channel.send('https://www.youtube.com/watch?v=bYtEfMMVjb8')

    elif message.content == '!tradingview':
        await message.channel.send('https://www.youtube.com/watch?v=Jlwp_ti9X-4')

    elif message.content == '!fibonacci':
        await message.channel.send('https://www.youtube.com/watch?v=gP1g3OrsfnY')

    elif message.content == '!indicator':
        await message.channel.send('https://www.youtube.com/watch?v=F_sUv770l0E')
        await message.channel.send('https://www.youtube.com/watch?v=bF_LwPuZJ10')
        await message.channel.send('https://www.youtube.com/watch?v=h_zNMesrYDw')
        await message.channel.send('https://www.youtube.com/watch?v=lrhPHSC6j4w')

    elif message.content == '!divergence':
        await message.channel.send('https://www.youtube.com/watch?v=DS_cZ3SeHtE')

    elif message.content == '!morningmoon':
        await message.channel.send('https://www.youtube.com/watch?v=d50mVHWf_x8')
        await message.channel.send('https://www.youtube.com/watch?v=eAtJetlwKqM&t=6s')
        await message.channel.send('https://www.youtube.com/watch?v=jQrT7eyh2vA&t=453s')

    elif message.content == '2+2':
        await message.channel.send('หน้าเหมือนเครื่องคิดเลขหรอ?')
        
    elif message.content == '!menu':
        await message.channel.send('Cyptuay ขอแนะนำ')
        await message.channel.send('ใส่!หน้าคำสั่ง')
        await message.channel.send('newbie')
        await message.channel.send('future')
        await message.channel.send('bitkub')
        await message.channel.send('tradingview')
        await message.channel.send('fibonacci')
        await message.channel.send('indicator')
        await message.channel.send('divergence')


    elif message.content == '!logout':
        await bot.logout()
    await bot.process_commands(message)

bot.run('OTA2NzExNDc1MzMzMjUxMDgy.YYcm3Q.WkeVJY9jVE1SJSKYcJw_gbb3jw4')