#!/usr/bin/env python
import asyncio
import tomli
from bot import AelstunBot

try:
    import uvloop # type: ignore
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

with open('config.toml', 'rb') as stream:
    config = tomli.load(stream)



