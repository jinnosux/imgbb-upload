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

if key == None:
    print("Token not loaded/found. Aborting")
    exit()

yes = {'yes','y', 'ye', ''}
image_folder = "./images/"
image_rand = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnm') for i in range(8)))
image_name = image_folder + image_rand + ".png"

def copy_image_from_clipboard():
    im = ImageGrab.grabclipboard()

    try:
        print("Copying image from clipboard...")
        im.save(image_name,'PNG')
        time.sleep(1)
    except AttributeError:
        print("Looks like clipboard is empty.")
        exit()


async def upload_to_imgbb(image,name):
    print("Uploading Image...")
    session = aiohttp.ClientSession()
    imgbb = Client(key,session)

    response = await imgbb.post(image,name)
    url = response['data']['url']

    pyperclip.copy(url)
    print(f'Uploaded image URL({url}) copied to clipboard.')
    await session.close()


if __name__=='__main__':
    copy_image_from_clipboard()
    asyncio.run(upload_to_imgbb(image_name,image_rand))

    print("Want to delete local image (y/n) ?")
    choice = input().lower()
    if choice in yes:
        if os.path.exists(image_name):
            os.remove(image_name)
        print("Image deleted locally.")
    else:
        exit()
