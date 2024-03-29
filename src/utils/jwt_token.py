import os
from datetime import datetime, timedelta
from typing import Any, Dict
from jose import jwt

secret_key = os.environ.get("SECRET_KEY")

async def genereate_accesstoken(userdata: Dict[str, Any]) -> str:
    token = jwt.encode(
        {
            "username": userdata["username"],
            "id": userdata["id"],
            "exp": datetime.utcnow() + timedelta(hours=1),
            # "expires": time.time() + 600, # this is using python time module
        },
        key=str(secret_key),
        algorithm="HS256",
    )
    return token


async def decode_accesstoken(token: str) -> Dict[str, Any]:
    decoded_val = jwt.decode(token, str(secret_key))
    return decoded_val
