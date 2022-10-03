from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules import auth
from src.utils.prisma import prisma


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)


@app.on_event("startup")
async def handle_start():
    await prisma.connect()


@app.on_event("shutdown")
async def handle_stop():
    await prisma.disconnect()


@app.get("/")
async def get_home_handler():
    return {"message": "hello world"}

app.include_router(auth.router)
