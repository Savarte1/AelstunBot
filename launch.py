#!/usr/bin/env python

import tomli

with open('config.toml', 'rb') as stream:
    BotSettings = tomli.load(stream)

