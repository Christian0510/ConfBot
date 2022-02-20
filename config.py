from config_example import Config


class Development(Config):
    # TOKEN del bot a usar: dado por @botfather
    TOKEN = Config.TOKEN or ''

    # ID del canal a usar, se obtiene annadiendo el bot al canal y  escribiendo help ( borre las comillas,
    # la data recibida tiene que ser un int )
    CHANNEL_ID = Config.CHANNEL_ID or ''

    # ID del grupo de administradores que manejaran la confesion. ( borre las comillas, la data recibida tiene que
    # ser un int )
    ADMIN_GROUP_ID = Config.ADMIN_GROUP_ID or ''
