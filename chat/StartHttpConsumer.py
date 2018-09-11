import asyncio
from channels.generic.http import AsyncHttpConsumer


class RootHttpConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        await asyncio.sleep(10)
        await self.send_response(200, b"Your response bytes", headers=[
            ("Content-Type", "text/plain"),
        ])

