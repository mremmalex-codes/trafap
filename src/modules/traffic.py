from datetime import datetime
from typing import Optional
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from src.utils.prisma import prisma

router = APIRouter(prefix="/traffic")


class Traffic(BaseModel):
    """
    this mocks the data  to receive for the creation of a new traffic
    """

    location: str
    description: str
    priroity: str = "N/A"
    start: Optional[datetime]
    stop: Optional[datetime]


class UpdateTraffic(BaseModel):
    status: str


@router.get("/search/")
async def handle_traffic_search(query: str):
    """
    this endpoint handles the search of a traffic update
    based by the location
    """
    if not query:
        return JSONResponse(
            {
                "message": "Search Param is required",
                "statusCode": status.HTTP_400_BAD_REQUEST,
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
                "statusCode": status.HTTP_404_NOT_FOUND,
                "data": None,
                "error": True,
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )

    json_comp_data = jsonable_encoder(results)

    return JSONResponse(
        {
            "message": "Traffic Data  Found",
            "statusCode": status.HTTP_200_OK,
            "data": json_comp_data,
            "error": False,
        },
        status_code=status.HTTP_200_OK,
    )


@router.post("/addUpdate")
async def handle_adding_traffic_update(update: Traffic) -> JSONResponse:
    """
    this endpoint handles the the adding of new traffic
    update and saving to the database if the infos are all correct
    """
    result = await prisma.traffic.create(
        data={
            "location": update.location,
            "message": update.description,
            "start": update.start,
        }
    )

    json_comp_data = jsonable_encoder(result)

    return JSONResponse(
        {
            "message": "Traffic Found",
            "statusCode": status.HTTP_200_OK,
            "data": json_comp_data,
            "error": False,
        },
        status_code=status.HTTP_200_OK,
    )


@router.patch("/updateTrafficInfo/{id}")
async def handle_traffic_data_update(id: int) -> JSONResponse:
    """
    this endpoint takes a traffic id and updates
    changing the status if there is no more traffic in
    that area
    """
    result = await prisma.traffic.find_unique(where={"id": id})
    if not result:
        return JSONResponse(
            {
                "error": True,
                "statusCode": status.HTTP_404_NOT_FOUND,
                "data": None,
                "message": "no traffic data with this id",
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )
    json_serialize = jsonable_encoder(result)
    return JSONResponse(
        {
            "error": False,
            "statusCode": status.HTTP_200_OK,
            "data": json_serialize,
            "message": "traffic data updated successfully",
        },
        status_code=status.HTTP_200_OK,
    )


@router.get("/allTraffic")
async def handle_all_traffic(skip: int = 0, take: int = 9) -> JSONResponse:
    """
    this endpoint returns all the traffic in the database
    with 9 pagination
    """
    result = await prisma.traffic.find_many(
        skip=skip, take=take, cursor={"id": 1}, order={"id": "asc"}
    )
    if not result:
        return JSONResponse(
            {
                "error": True,
                "statusCode": status.HTTP_404_NOT_FOUND,
                "data": None,
                "message": "no traffic data yet",
            },
            status_code=status.HTTP_404_NOT_FOUND,
        )

    json_serialize = jsonable_encoder(result)

    return JSONResponse(
        {
            "error": True,
            "statusCode": status.HTTP_200_OK,
            "data": json_serialize,
            "message": "Traffics Found",
        },
        status_code=status.HTTP_200_OK,
    )
