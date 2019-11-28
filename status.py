# Work with Python 3.6
import discord
import os
from os import system
import time

system("title "+"Status Changer")

TOKEN = os.environ["BOT_TOKEN"]

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=""))
    print('다음 계정으로 로그인됨:')
    print(client.user.name)
    print(client.user.id)
    print('--- 동작 중 ---')
    i = 1
    while True:
        kame = "명령어는 \"명령어!\"로 확인!ㅤㅤㅤㅤ"
        await client.change_presence(game=discord.Game(name=kame))
        time.sleep(7)
        version = os.environ["VERSION"]
        kame = version + "ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ"
        await client.change_presence(game=discord.Game(name=kame))
        time.sleep(3)



client.run(TOKEN)
