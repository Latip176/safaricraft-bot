import discord
from discord.ext import commands
from utils import fetch_anime_api
from random import choice


class Anime(commands.Cog):
    
    async def fetch_data(self, path: str = "") -> dict:
        response = await fetch_anime_api(path=path)
        
        return response

class Commands(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def anime(self, ctx, category: str, *, value: str = ""):
        anime = self.client.get_cog("Anime")
        try:
            if anime is not None:
                if category == "":
                    path = "/"
                    response = await anime.fetch_data(path=path)

                    first_anime = response['data']['data'][0]
                elif category == "ongoing":
                    path = "/api/otakudesu/ongoing/" + (f"?next=page-{value}" if value != "" else "")
                    response = await anime.fetch_data(path=path)

                    first_anime = choice(response['data']['data_anime'])
                elif category == "search":
                    path = "/api/otakudesu/search/?keyword=" + value
                    response = await anime.fetch_data(path=path)

                    first_anime = response['data']['data'][0]
                
                cover_url = first_anime['cover']
                title = first_anime['judul']
                data = first_anime['data']
                
                try:
                    genres = first_anime['genres']
                    rating = first_anime['rating']
                    status = first_anime['status']
                except:
                    genres = "-"
                    rating = "-"
                    status = "ongoing"
    
                embed = discord.Embed(
                    title=title,
                    url=f"https://latipnime.netlify.app/#info?data={data}",
                    description=f"Data: {data}\nGenres: {genres}\nRating: {rating}\nStatus: {status}",
                )
                embed.set_thumbnail(url=cover_url)
                
                await ctx.send(embed=embed)
        except discord.DiscordException as e:
            print("DiscordException:", e)
            await ctx.send("An error occurred while sending the response.")
        except Exception as e:
            print("General Exception:", e)
            await ctx.send("An unexpected error occurred.")


        
            
async def setup(client):
    await client.add_cog(Anime(client))
    await client.add_cog(Commands(client))