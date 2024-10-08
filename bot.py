import discord
from discord.ext import commands
from config import TOKEN, PREFIX, INTENTS
import asyncio

client = commands.Bot(command_prefix=PREFIX, intents=INTENTS)

@client.event
async def on_ready():
    print("[SafariCraft BOT] Started")
    print("==========================")
    for extension in ["cogs.player_status", "cogs.commands"]:
        try:
            await client.load_extension(extension)
            print(f"Successfully loaded extension: {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")

async def main():
    async with client:
        await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
