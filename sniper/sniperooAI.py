from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
import asyncio

"""
import logging
logging.basicConfig(format='[%(levelname) %(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
"""

apiID = 28083364
apiHash = 'cb5bedddad06f7772cb1376e2d979465'
sessionPath = r'C:\Users\juliu\Desktop\A- PYHTON\sniper\sniperooAI'
client = TelegramClient(sessionPath, apiID, apiHash)

gemID = -1001998961899
sonicID = -1002135104289

@client.on(events.NewMessage(chats=PeerChannel(gemID)))
async def handler(event):
    message = event.text.split('\n')
    for i in message:
        print(i)
    
@client.on(events.NewMessage(chats=PeerChannel(sonicID)))
async def handler2(event):
    message = event.text.split('\n')
    await client.forward_messages('me', event.message)

async def main():
    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
