import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}

#:::::::::::::@OFFICIALHACKERERA

API_ID = int(getenv("API_ID", "14964504"))

API_HASH = getenv("API_HASH", "7ddc2e405de3b79daa752d971f3336b8")

BOT_TOKEN = getenv("BOT_TOKEN", "7576028028:AAFbSQFeStfHVdbAyLrMuMgFqh-FhFMEjcs")

DEEPAK_SESSION = getenv("DEEPAK_SESSION", "BQDkVxgAVByicTqSuqnkTwrIFXhJLvMJ2pGwpPBP41HKkZuctVup5H-qR-IKxTxmT8jzIlhBYn4WWM_ZdBmroWAKBXxGSxstT5aTqupiN4KbYPj389PgMml4jSdosEq-HKM5j7_1azHDzhIYqnGiwX33FMGOQIRTIcLRwfa5NzFF7OqNZeZKLrGcDvbVX4iu62AezsHt3jATF6mVCs5Me2Yscr5a9auRQJ26rZM__NyeSte82BwywUxD0KndBE_sHNZeTn-w3csdaKO5rhC61A5CaDe00zgbFHjha74w2atXi0jrSu7DrUJdz37N0NibLdG8W3bncfY-ekEVZjuV52dJwrc2_wAAAAHOQYzfAA")

OWNER_ID = getenv("OWNER_ID", "2035388821")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002369007076"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6508157803").split()))

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://noob43597:Kq38rKvmP7ScCBYQ@frozenbots.hf0o4fn.mongodb.net/")

OWNER_NAME = getenv("OWNER_NAME", "OFFICIALHACKERERA")

BOT_NAME = getenv("BOT_NAME", "Ultra X Music")

ASSISTANT_NAME = getenv("ASSISTANT_NAME", "hbh")

GROUP_SUPPORT = getenv("GROUP_SUPPORT", "gvv")

UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ggvv")

OWNER_USERNAME = getenv("OWNER_USERNAME", "raox")

ALIVE_NAME = getenv("ALIVE_NAME", "bb")

BOT_USERNAME = getenv("BOT_USERNAME", "gvvv")






UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ANIL-XD/A-X-MUSIC-BOT")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "master")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5000"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/ab04d080f30e7a7f91991.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/ab04d080f30e7a7f91991.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
EMOJI = getenv("EMOJI", "🥀")
