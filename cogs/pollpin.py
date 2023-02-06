from discord.ext import commands
import discord
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot import AelstunBot

class PollPin(commands.Cog):
    """A cog to generate pins for voting ballots using forms"""

    def __init__(self, bot: AelstunBot):
        self.bot = bot


