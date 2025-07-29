from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    async def handle(self, action: str, parameters: dict) -> dict:
        pass