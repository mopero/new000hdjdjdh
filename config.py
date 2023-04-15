from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "19425462")
APP_HASH = os.environ.get("APP_HASH", "a859a87bcc16d1021148a245b4bea2d6")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "is3BoDebot")
session = os.environ.get("TERMUX", "1ApWapzMBuzKe8XPhDJXzTj4hexMMdNicGqD399bd_rni4HkM3gxEl2PJOHAxS5p02jIq6zY-Ss7tPH9zseJkTanXx-LkPZlNf6IrAebsmDA38HZKh52UZLTly_De6a9Su3_YptQt2CVo8THAD5pirqSDgHvoYfJYS6fp_tKcr98A5RPC8u9fYARe6wvqm3_R4zl64SectMDwga-D4zuWk1fgb1saYaWsZslZr8d3DWi76ika3qDBz-qFZm3XXBN8QUkgkHlVOBiv90FN34nq9c_JeGeC9qEWz51EigVy_GEDFpnhCo7-asOhKAyWPtzKXPj73gwVBH_SHTI5KXcDQ25LvJME4bI=")
SESSION = os.environ.get("TERMUX", "1ApWapzMBuzKe8XPhDJXzTj4hexMMdNicGqD399bd_rni4HkM3gxEl2PJOHAxS5p02jIq6zY-Ss7tPH9zseJkTanXx-LkPZlNf6IrAebsmDA38HZKh52UZLTly_De6a9Su3_YptQt2CVo8THAD5pirqSDgHvoYfJYS6fp_tKcr98A5RPC8u9fYARe6wvqm3_R4zl64SectMDwga-D4zuWk1fgb1saYaWsZslZr8d3DWi76ika3qDBz-qFZm3XXBN8QUkgkHlVOBiv90FN34nq9c_JeGeC9qEWz51EigVy_GEDFpnhCo7-asOhKAyWPtzKXPj73gwVBH_SHTI5KXcDQ25LvJME4bI=")
token = os.environ.get("TOKEN", "6268667114:AAGuyDqRth3_H9qbAiQuNwtDsEMv3UPPCJ8")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
