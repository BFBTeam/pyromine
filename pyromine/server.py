import base64
import os
from pathlib import Path

from logzero import logger

from pyromine.utils.config import Config


class Server:
    def __init__(self, data_path, plugin_path):
        try:
            if not Path(data_path + "worlds/").is_dir():
                os.mkdir(data_path + "worlds/", 0o777)
            if not Path(data_path + "players/").is_dir():
                os.mkdir(data_path + "players/", 0o777)
            if not Path(plugin_path).is_dir():
                os.mkdir(plugin_path, 0o777)

            self.data_path = os.path.realpath(data_path)
            self.plugin_path = os.path.realpath(plugin_path)

            """pyromine.yml"""
            logger.info("Loading pyromine.yml")

            """language support"""
            try:
                pass
            except FileNotFoundError as e:
                logger.warning("Fallback language")
                return

            logger.info("Loading server properties...")
            self.properties = Config(self.data_path + "server.properties", Config.PROPERTIES, {
                "motd": "Pyromine Server",
                "server-port": 19132,
                "whitelist": False,
                "announce-player-achievements": True,
                "spawn-protection": 16,
                "max-players": 20,
                "spawn-animals": True,
                "spawn-mobs": True,
                "gamemode": 0,
                "force-gamemode": False,
                "hardcore": False,
                "pvp": False,
                "difficulty": 1,
                "generator-settings": "",
                "level-name": "world",
                "level-seed": "",
                "level-type": "DEFAULT",
                "enable-query": True,
                "enable-rcon": False,
                "rcon.password": base64.b64encode(os.urandom(20))[3:10],
                "auto-save": True,
                "view_distance": 8,
                "xbox-auth": True
            })

            # memory manager
            # here >>

            logger.info("pocketmine.server.start")







        except Exception as e:
            logger.error(e)
            pass