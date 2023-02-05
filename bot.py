import discord
from discord.ext import commands
from sans.api import Api


class AelstunBot(commands.Bot):

    def __init__(self, config):
        super().__init__(command_prefix=config["bot"]["prefix"], intents=discord.Intents.all())
        self.config = config
        Api.loop = self.loop
        Api.agent = f'{config["nationstates"]["agent"]} (AelstunBot/1.0a)'

    async def start(self):
        await super().start(self.config["bot"]["token"], reconnect=True)



