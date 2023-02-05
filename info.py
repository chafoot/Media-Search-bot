import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['27709822'])
API_HASH = environ['a30de8d316e15153c76c64342b86546b']
BOT_TOKEN = environ['5834534987:AAFYzz6Ptke3GSaRviaeLMBhwp5Kwg9MZNY']
USERBOT_STRING_SESSION = environ.get('BQDBAcaxs8BDAwths52aqd134P_4cLMBJdiR2h5o3f0kre5pIYUu25iwoDDslQOvOcZArIbJ9S-fkc6NIKcwwAjAEttgzK2L2t6d1k6jyyR0OIweMhApvoAnrXrWeuyh3qCrbShsZ1KdAFGjhup-o95nyra6ocVJHUNOLauVveZGaYmhDHw_k8y1ewPPy-qCBjL0u2XsVJrsP98xaU3g48_P_2vc23tmEHMrRdv5VFv2N9leUfskTnjgVjOzmx4cvLNjDMb2z1-Fw2lpFm0oQV7u9TYaoWSNPKlc_wRr-yvsq6f5TDTosjVJLl2lb_8b4HFjXntKOgXSsvvKGmaUundlAAAAAUalmTAA')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['mongodb+srv://chafoot:aruntokumar@cluster0.knowtcs.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['cluster0']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
