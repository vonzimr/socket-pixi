from aiohttp import web


async def create_app():
    from backend.app.websocket import websocket_handler

    app = web.Application()
    app.add_routes([web.get('/ws', websocket_handler)])
    return app
