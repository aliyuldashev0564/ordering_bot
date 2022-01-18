import aiohttp
from config import agent_url, product_url
async def aget():
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(agent_url) as res:
            return await res.json()

async def product():
    async with aiohttp.ClientSession() as session:
        async with session.get(product_url) as result:
            return await result.json()