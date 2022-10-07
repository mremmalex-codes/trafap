from datetime import datetime
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from src.utils.prisma import prisma

router = APIRouter(prefix="/traffic")


class Traffic(BaseModel):
    location: str
    message: str
    start: datetime
    stop: datetime


@router.post("/search/")
async def handle_traffic_search(query: str):
    if not query:
        return JSONResponse(
            {
                "message": "Search Param is required",
                "statuscode": status.HTTP_400_BAD_REQUEST,
                "data": None,
                "error": True,
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    results = await prisma.traffic.find_many(where={"location": query})

    if not results:
        return JSONResponse(
            {
                "message": "No Result Found For This Search Query",
                "statuscode": status.HTTP_404_NOT_FOUND,
                "data": None,
                "error": True,
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )

    json_comp_data = jsonable_encoder(results)

    return JSONResponse(
        {
            "message": "Traffic Found",
            "statusCode": status.HTTP_200_OK,
            "data": json_comp_data,
            "error": False,
        },
        status_code=status.HTTP_200_OK,
    )


@router.post("/addUpdate")
async def handle_adding_traffic_update(update: Traffic) -> JSONResponse:
    result = await prisma.traffic.create(
        data={
            "location": update.location,
            "message": update.message,
            "start": update.start,
        }
    )

    json_comp_data = jsonable_encoder(result)

    return JSONResponse(
        {
            "message": "Traffic Found",
            "statuscode": status.HTTP_200_OK,
            "data": json_comp_data,
            "error": False,
        },
        status_code=status.HTTP_200_OK,
    )


@router.patch("/addUpdate/{pk}")
async def handle_traffic_data_update(pk: int) -> JSONResponse:
    result = await prisma.traffic.find_unique(where={"id": pk})
    json_serialze = jsonable_encoder(result)
    return JSONResponse(json_serialze)
