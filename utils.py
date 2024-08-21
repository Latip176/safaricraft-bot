import aiohttp

async def fetch_server_status() -> dict:
    url = "https://mc-server-status-seven.vercel.app/api/java?ip=play.safaricraft.my.id:19132"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as resp:
            return await resp.json()
        
async def fetch_anime_api(path: str = "") -> dict:
    url = "https://latipharkat-api.my.id" + path
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as resp:
            return await resp.json()
