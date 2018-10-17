import asyncio
import logging
from flask import Flask
from .cron import start_cron

log = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


async def start_app():
    app.run('0.0.0.0', port=8080)


if __name__ == "__main__":
    loop = asyncio.get_default_loop()

    asyncio.ensure_future(start_cron(), loop)
    sleep(1)
    asyncio.ensure_future(start_app(), loop)

    loop.run_forever()
