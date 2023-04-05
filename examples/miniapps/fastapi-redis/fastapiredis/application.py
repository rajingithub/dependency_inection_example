"""Application module."""

from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI, Depends, Request

from containers import Container
import endpoints


def create_app() -> FastAPI:
    container = Container()
    container.config.redis_host.from_env("REDIS_HOST", "localhost")
    container.config.redis_password.from_env("REDIS_PASSWORD", "password")

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


app = create_app()


####################################################################################
#                                     IMPORTANT                                    #
# This middleware runs after every request and resets the config service instance. #
# This will make sure we have a scoped singleton instance of config service for    #
# every request.                                                                   #
####################################################################################
@app.middleware("http")
async def reset_config_scope(request: Request, call_next):
    response = await call_next(request)
    app.container.config_service.reset()
    return response
