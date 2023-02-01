from discord.ext import commands, tasks
from ..bot import AelstunBot


class NSCore(commands.Cog):

    def __init__(self, bot: AelstunBot):
        self.bot = bot
