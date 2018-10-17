import asyncio
import logging

log = logging.getLogger(__name__)


async def start_cron():
    i = 0
    while 1:
        i += 1
        log.info("Cron logging %d" % i)
        await asyncio.sleep(0.1)
