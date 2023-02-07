from functools import wraps

# from fastapi.

def required_user(func):
    """
    creating a middleware that will check if the user
    is authenticated by verifying the access token passed in the header
    and the cookie
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        pass
