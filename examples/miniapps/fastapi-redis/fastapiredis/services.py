"""Services module."""

from aioredis import Redis


class ConfigService:
    def __init__(self, redis: Redis) -> None:
        print("ConfigService init")
        self._redis = redis
        self.store = None
        self.config_data = None

    async def process(self) -> str:
        await self._redis.set("my-key", "value")
        return await self._redis.get("my-key")
    
    async def get_value(self,name):
        return await self._redis.get(name)
    
    async def set_value(self, key, value):
        return await self._redis.set(key, value)

    async def set_name(self,name):
        self.store = name
        self.config_data = await self.get_value(self.store)

class ProductService:
    def __init__(self, config: ConfigService):
        print("ProductService init")
        self._config = config

    def get(self):
        return self._config.config_data
