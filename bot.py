import discord
from discord.ext import commands
from sans.api import Api


class AelstunBot(commands.Bot):

    def __init__(self, config):
        super().__init__(command_prefix=config["bot"]["prefix"], intents=discord.Intents.all())
        Api.loop = self.loop
        Api.agent = config["nationstates"]["agent"]



