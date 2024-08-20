from discord.ext import commands
from utils import fetch_server_status

class PlayerStatus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        questions = [
            "ada berapa yang on?",
            "siapa saja yang online?",
            "berapa orang yang online?",
            "ada yang online gak?",
            "siapa yang lagi on?",
            "online berapa orang?",
            "berapa yang lagi on?",
            "ada siapa yang online?"
        ]

        if any(question in message.content.lower() for question in questions):
            try:
                response = await fetch_server_status()
                players = response["data"]["players"]
                online = players["online"]
                max_online = players["max"]

                await message.reply(f"Hallo {message.author.mention}, yang on ada {online} / {max_online} players!")
            except Exception as e:
                await message.reply(f"Maaf, terjadi kesalahan saat mengambil data server: {e}")

async def setup(client):
    await client.add_cog(PlayerStatus(client))
