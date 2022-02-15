from config_example import Config


class Development(Config):
    TOKEN = Config.TOKEN or ''  # TOKEN del bot a usar: dado por @botfather

    CHANNEL_ID = Config.CHANNEL_ID or ''  # ID del canal a usar, se obtiene annadiendo el bot al canal y escribiendo
                                            # help ( borre las comillas, la data recibida tiene que ser un int )

    SUDO_USERS = Config.SUDO_USERS or []  # Lista de IDs que sean administradores o que vayan a manejar las Confesiones
