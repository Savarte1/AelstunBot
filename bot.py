import discord
from discord.ext import commands
from sans.api import Api


class AelstunBot(commands.Bot):

    def __init__(self, config: dict):
        super().__init__(command_prefix=config["bot"]["prefix"], intents=discord.Intents.all())
        self.config = config
        Api.loop = self.loop
        Api.agent = f'{config["nationstates"]["agent"]} (AelstunBot)'

    async def start(self, **kwargs):
        await super().start(self.config["bot"]["token"], reconnect=True)

    async def setup_hook(self):
        await self.load_extension('cogs.general')
