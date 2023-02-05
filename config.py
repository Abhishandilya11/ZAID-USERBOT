import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "995191846").split()))
OWNER_ID = int(getenv("OWNER_ID","995191846"))
MONGO_URL = getenv("MONGO_URL","mongodb+srv://Jubin:<password>@cluster0.tmyxn24.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6032456716:AAFSEWNktQ-uPA1K9QQQpnVPwLWr8ktBWlY")
ALIVE_PIC = getenv("ALIVE_PIC",)
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAL8LLGVhhED4uATEF2QQsB5_7XzgKVkDnO9IYt_PxgWc9F8_fY4Rwchiu6xTYG9EdyKlfhwRIYXdfRGL9MV4FsrhdKQ7c9_XaUR_IK3L8izqr8yWFyzxiDIa-XPsujPqqyM5dmo9EbvBJGbHW2rucdIMBtwci7cqhjlTSYGPm2mmgTwRL3PiPkpBBybkUS3S62i70k5dRF8_5lfq5t4W7yyXlsGGmavocXlYyl200aLVITzU6UCtVOIwjWJRyRqDO5kF-yVEFLEFAwFgZM998JKyqZOyJSNtZkTTUSFPGFlwN8L_mfcmMWIobKnW-RbdaW3EZEMAhvBLKVPe-EgBMRgAAAAA7UWwmAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
