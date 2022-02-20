import os
import json

# Solo si se prefiere usar un JSON en lugar de un archivo de configuracion de python
def get_data(key):
    with open('db/sudo_users.json', 'r') as file:
        return json.load(file)[key]


class Config(object):
    TOKEN = os.getenv('BOT_TOKEN')

    CHANNEL_ID = os.getenv('CHANNEL_ID')

    ADMIN_GROUP_ID = os.getenv('ADMIN_GROUP_ID')
