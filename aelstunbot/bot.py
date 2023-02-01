import discord
from discord.ext import commands


class AelstunBot(commands.Bot):

    def __init__(self, config):
        super().__init__(intents=discord.Intents.all())
