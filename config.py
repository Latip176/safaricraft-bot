import os
from dotenv import load_dotenv
import discord

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = "!"
INTENTS = discord.Intents.default()
INTENTS.message_content = True
