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
