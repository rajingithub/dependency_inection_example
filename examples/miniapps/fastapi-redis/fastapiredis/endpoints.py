"""Endpoints module."""

from typing import Optional, List

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from containers import Container
from services import ProductService, ConfigService

router = APIRouter()


@router.api_route("/")
@inject
async def index(service: ConfigService = Depends(Provide[Container.config_service])):
    return {"result": value}


@router.api_route("/name")
@inject
async def index(
        name,
        product_service: ProductService = Depends(Provide[Container.product_service]),
        config_service: ConfigService = Depends(Provide[Container.config_service])
):
    await config_service.set_name(name)
    return {"result": product_service.get()}


@router.api_route("/set-name")
@inject
async def index(
        key,
        value,
        config_service: ConfigService = Depends(Provide[Container.config_service])
):
    await config_service.set_value(key, value)
    return {"result": "ok"}
