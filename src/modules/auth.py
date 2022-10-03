
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import pydantic
from src.utils.prisma import prisma

router = APIRouter(
    prefix="/auth"
)

password_hasher = PasswordHasher()


class RegisterData(pydantic.BaseModel):
    username: str
    password: str
    email: pydantic.EmailStr


class LoginData(pydantic.BaseModel):
    username: str
    password: str


@router.post("/register")
async def register_handler(data: RegisterData):

    if len(data.username) < 1:
        return JSONResponse({"message": "Username Field Is Required",
                             "data": None, "error": True,
                             "statusCode": status.HTTP_400_BAD_REQUEST},
                            status_code=status.HTTP_400_BAD_REQUEST)

    if len(data.password) < 6:
        return JSONResponse({"message": "Password Field Is Required",
                             "data": None, "error": True,
                            "statusCode": status.HTTP_400_BAD_REQUEST},
                            status_code=status.HTTP_400_BAD_REQUEST)

    is_username_exist = await prisma.user.find_unique(
        where={
            'username': data.username
        }
    )

    is_email_exist = await prisma.user.find_unique(
        where={
            "email": data.email
        }
    )

    if is_username_exist:
        return JSONResponse({"message": "User with this username already exist",
                             "data": None, "error": True,
                             "statusCode": status.HTTP_400_BAD_REQUEST},
                            status_code=status.HTTP_400_BAD_REQUEST)

    if is_email_exist:
        return JSONResponse({"message": "User with this email already exist",
                             "data": None, "error": True,
                             "statusCode": status.HTTP_400_BAD_REQUEST},
                            status_code=status.HTTP_400_BAD_REQUEST)

    hash_password: str = password_hasher.hash(data.password)

    user = await prisma.user.create(
        data={
            "username": data.username,
            "password": hash_password,
            "email": data.email,
        }
    )
    return JSONResponse({"message": "Account Created",
                        "error": False,
                         "statusCode": status.HTTP_201_CREATED,
                         "data": {
                             "username": user.username,
                             "email": user.email,
                         }}, status_code=status.HTTP_201_CREATED)


@router.post("/login")
async def login_handler(data: LoginData):
    is_user_exits = await prisma.user.find_unique(
        where={
            "username": data.username
        }
    )

    if not is_user_exits:
        return JSONResponse({"message": "user with this username does not exist",
                             "data": None, "error": True,
                             "statusCode": status.HTTP_400_BAD_REQUEST},
                            status_code=status.HTTP_400_BAD_REQUEST)
    try:
        is_password_match = password_hasher.verify(
            is_user_exits.password, data.password)

        if is_password_match:

            return JSONResponse({"message": "login successful",
                                "error": False,
                                 "data": {
                                     "username": is_user_exits.username
                                 },
                                 "statusCode": status.HTTP_400_BAD_REQUEST},
                                status_code=status.HTTP_400_BAD_REQUEST)
    except VerifyMismatchError:

        return JSONResponse({"message": "incorrect password",
                            "error": False,
                             "data": None,
                             "statusCode": status.HTTP_400_BAD_REQUEST},
                            status_code=status.HTTP_400_BAD_REQUEST)
