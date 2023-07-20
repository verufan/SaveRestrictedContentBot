#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("20047995", default=None, cast=int)
API_HASH = config("585b93fd73853e393c564b80c81ea550", default=None)
BOT_TOKEN = config("6384237561:AAHdOivkwPps2GllgEWHtBGcZbgdHvL5xro", default=None)
SESSION = config("BAEx6HsAndO86Z1z9Zs1VBJy4_zp9CYuMNCPVKIkL12LAV2pfhKBDzGJaG-u_Pgq72W8Rd7iYK24PBDfqF0iR7MoHpHwqeoU6cWw5iMqdAO0l4rFqklQZ44kGf56AB2yq57YyYTu7qKqZ6aA_2ZakWPdqnKygDcIBb_Ptr9UZa1RndmGj2DYabywsRXIw7WQ39g5f-6CVScD2hzMyTolK6AlrGnj7UKNpHow96iwbr8CnOu_ZRPQXNIq4fvtCtIJ1O_9DJONVrh9nrub0YYKefmqgHQg5aaYKaMVaGU7HekM08wNkgTMULbOkTLJr5NQ3XVlzQgXQeG00oZAJcAbGaH2QWIXywAAAAFxB_KYAA", default=None)
FORCESUB = config("colongcontenbot", default=None)
AUTH = config("6191313560", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
