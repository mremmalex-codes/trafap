from typing import Any, Dict
import os
from jose import jwt
import time

secret_key = os.environ.get("SECRET_KEY")


async def genereate_accesstoken(userdata: Dict[str, Any]) -> Any:
    token = jwt.encode(
        {
            "username": userdata["username"],
            "id": userdata["id"],
            "expires": time.time() + 600,
        },
        key=str(secret_key),
        algorithm="HS256",
    )
    return token


async def decode_accesstoken(token: str) -> Dict[str, Any]:
    decoded_val = jwt.decode(token, str(secret_key))
    return decoded_val
