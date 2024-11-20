# Don't Remove Credit @Shankar_Kola
# Subscribe YouTube Channel For Amazing Bot @achievers_base
# Ask Doubt on telegram @Time2ChillBot

from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
