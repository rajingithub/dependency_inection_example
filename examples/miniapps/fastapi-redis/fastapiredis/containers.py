"""Containers module."""

from dependency_injector import containers, providers
import redis, services


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["endpoints"])

    config = providers.Configuration()

    redis_pool = providers.Resource(
        redis.init_redis_pool,
        host="127.0.0.1"
    )

    config_service = providers.Singleton(
        services.ConfigService,
        redis=redis_pool,
    )

    product_service = providers.Factory(
        services.ProductService,
        config=config_service,
    )
