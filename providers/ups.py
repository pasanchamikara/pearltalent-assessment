import asyncio
from .base import BaseProvider

class UPSProvider(BaseProvider):
    async def handle(self, action: str, parameters: dict) -> dict:
        await asyncio.sleep(0.5)
        xml_like_response = f"<response><status>success</status><action>{action}</action></response>"
        return {"ups_xml": xml_like_response}