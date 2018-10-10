import aiohttp
from aiohttp import web
import asyncio

clients = {} 
async def notify_clients(this_client):
    for client in clients.values():
        if client.cid == this_client.cid:
            continue
        else:
            await client.notify(this_client)


async def create_app():
    app = web.Application()
    app.add_routes([web.get('/ws', websocket_handler)])
    return app
