import aiohttp

async def fetch_server_status():
    url = "https://mc-server-status-seven.vercel.app/api/java?ip=play.safaricraft.my.id:19132"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
