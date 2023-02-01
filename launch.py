#!/usr/bin/env python

import tomli
import asyncio
import discord
import logging

from aelstunbot.bot import AelstunBot

with open('config.toml', 'rb') as stream:
    BotSettings = tomli.load(stream)

