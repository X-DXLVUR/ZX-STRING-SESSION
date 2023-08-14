from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24854614"))
API_HASH = getenv("API_HASH", "bb4a375c908f0681ed4083f4fb3a9ced")

BOT_TOKEN = getenv("BOT_TOKEN", "6029802782:AAHHUAVtZofsLn6Sj3JVYT5BUdqeJlQF-9E")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6164559838))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/soul_x6")
