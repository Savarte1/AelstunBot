#!/usr/bin/env python
import asyncio
import tomli
import discord
from bot import AelstunBot

try:
    import uvloop # type: ignore
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

with open('config.toml', 'rb') as stream:
    config = tomli.load(stream)


def launch():
    async def launch_bot():
        async with AelstunBot(config) as bot:
            await bot.start()

    discord.utils.setup_logging()

    try:
        asyncio.run(launch_bot())
    except KeyboardInterrupt:
        return


launch()

