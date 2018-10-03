import aiohttp
from aiohttp import web
import asyncio
import secrets
import struct

clients = {}
pos = struct.Struct("<II")

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print("Web socket connection ready")
    id = request.headers.get('sec-websocket-key')
    print("Client Connected with id {}".format(id))

    async for msg in ws:
        print(msg)
        if msg.type == aiohttp.WSMsgType.BINARY:
            clients[id] = pos.unpack(msg.data)
            print("New Pos: {}".format(clients[id]))
        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
    return ws

app = web.Application()

app.add_routes([web.get('/ws', websocket_handler)])
