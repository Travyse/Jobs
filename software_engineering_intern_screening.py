import asyncio
import logging
import os # os wasn't imported
from datetime import datetime # datetime wasn't imported

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")

class Pipeline:
    async def __init__(self, *args, **kwargs):
        self.default_sleep_duration = kwargs["default_sleep_duration"]
        # Assign the default_sleep_duration value to an attribute

    async def sleep_for(coro, sleep_duration, *args, **kwargs):
        asyncio.sleep(sleep_duration)
        logger.info("Slept for %s seconds", sleep_duration) #improper indentation
        start = datetime.now()
        await coro(*args, **kwarg)
        end = datetime.now()
        time_elapsed = (start - end).total_seconds()
        logger.debug(f"Executed the coroutine for {time_elapsed} seconds")
