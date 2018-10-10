import secrets
import struct
from aiohttp import web
import asyncio

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print("Web socket connection ready")
    id = request.headers.get('sec-websocket-key')
    print("Client Connected with id {}".format(id))
    client = Client(ws)
    clients[id] = client
    await notify_clients(client)

    async for msg in ws:
        print(msg)
        if msg.type == aiohttp.WSMsgType.BINARY:
            print("new message: ".format(msg.data))
            client.update_pos(msg.data)
            await notify_clients(client)

        if msg.type == aiohttp.WSMsgType.TEXT:
            print(msg.data)
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
    return ws
