from aiohttp import web
import aiohttp_jinja2
import asyncio
import random
import string
import time


CHARS = string.ascii_letters + string.digits

def generate_string():
    size = random.randint(1, 100)
    s = ''.join(random.choice(CHARS) for _ in range(size))
    return s

@aiohttp_jinja2.template('index.html')
async def index(request):
    return {}

async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    start_time = time.time()
    start_ms = start_time - int(start_time)

    while True:
        await ws.send_str(generate_string())
        t = time.time()
        sleep_time = 1 - (t-int(t)-start_ms)
        await asyncio.sleep(sleep_time)

    return ws

app = web.Application()
aiohttp_jinja2.setup(app, loader=aiohttp_jinja2.jinja2.FileSystemLoader('.'))
app.router.add_get('/', index)
app.router.add_get('/ws', ws_handler)

web.run_app(app)