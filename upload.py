from PIL import ImageGrab
from imgbb.client import Client
import time
import os
import aiohttp
import asyncio
import random
import base64
import requests
import pyperclip
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('imgbb-token')

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

image_folder = "./images/"
image_rand = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(8)))
image_name = image_folder + image_rand + ".png"
im = ImageGrab.grabclipboard()
try:
    print("Copying image from clipboard...")
    im.save(image_name,'PNG')
    time.sleep(1)
except:
    print("Looks like clipboard is empty.")
    exit()

async def upload(image,name):
    print("Uploading Image...")
    session = aiohttp.ClientSession()
    myclient = Client(key,session)
    response = await myclient.post(image,name)
    url = response['data']['url']
    pyperclip.copy(url)
    print(f'Uploaded image URL({url}) copied to clipboard.')
    await session.close()

if __name__=='__main__':
    asyncio.run(upload(image_name,image_rand))
    print("Want to delete local image (y/n) ?")
    choice = input().lower()
    if choice in yes:
        if os.path.exists(image_name):
            os.remove(image_name)
    elif choice in no:
        exit()
