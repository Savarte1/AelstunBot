from discord.ext import commands
import discord
from typing import TYPE_CHECKING
from bot import AelstunBot


class General(commands.Cog):
    """General commands"""

    def __init__(self, bot: AelstunBot):
        self.bot = bot

    @commands.hybrid_command()
    async def profile(self, ctx: commands.Context, user: discord.User = None):
        await ctx.send("Test")


async def setup(bot: AelstunBot):
    await bot.add_cog(General(bot))
