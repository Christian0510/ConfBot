import json

# Solo si se prefiere usar un JSON en lugar de un archivo de configuracion de python
def get_data(key):
    with open('db/sudo_users.json', 'r') as file:
        return json.load(file)[key]


class Config(object):
    TOKEN = get_data('token')

    CHANNEL_ID = get_data('channel')

    SUDO_USERS = get_data('sudo')
