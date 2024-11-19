import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "f2cd5ea2f572dd7442ebb57b3273fdfd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8072449817:AAHAm_bj7Qm8Xhzx6QkHCQHUII337kGfOis")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "23291389")
    OWNER = os.environ.get("OWNER", " 6045914761")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME" ,"MrSagar0")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://merge1:merge1@cluster0.s9ze9.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002123429789")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQFULg8AuikWv1pexla19PBxl8QPFH_k7XUcFC03gE0tJ6jQEkM7K1fpAEH9lySM4FlGRAtW48JEwa8DiKHdAfCtznAyHgeWN8Jbv0S6VhoLCyJkOu7H3szzzgyYSvZg-lElPjt5t9QCUP4End4LubqX2XEdBiKVBI9WS7JYOy4UdWjGi1fsnSL_xdKN5mtnSIFKQGkMaWGYmRuvA8x2UQj11AHp3SJ8xt5LdZCcyt_He1tkEx1WkFAaUOVxw2dLm9lq5-BXCKEdnk83dnBZsMnsnoAT24nOaQujdAfVOi2DVuYGWPYA9MyR7GJ5taxHNdFcZ2Q7Xo47z2aziywkFCRbVz3XegAAAAGac7wcAA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
