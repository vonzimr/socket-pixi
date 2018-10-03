import aiohttp
from aiohttp import web
import asyncio
import secrets
import struct

clients = {} 

class Client:
    pos = struct.Struct("<II")
    client_pos = struct.Struct("<III")
    
    def __init__(self, ws):
        self._ws = ws
        self.x = 0 
        self.y = 0 
        self.cid = secrets.randbits(32)
    
    def update_pos(self, b):
        self.x, self.y = self.pos.unpack(b)

    def get_pos(self):
        return self.client_pos.pack(self.cid, self.x, self.y)

    async def notify(self, client):
        print("Notifying {} of client: {}".format(self.cid, client))
        await self._ws.send_bytes(client.get_pos())

    def __repr__(self):
        return "{}|({},{})".format(self.cid, self.x, self.y)

    def __str__(self):
        return self.__repr__()

async def notify_clients(this_client):
    for client in clients.values():
        if client.cid == this_client.cid:
            continue
        else:
            await client.notify(this_client)

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

app = web.Application()

app.add_routes([web.get('/ws', websocket_handler)])
