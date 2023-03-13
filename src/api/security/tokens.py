from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import encode, decode

security = HTTPBearer()
credential = HTTPAuthorizationCredentials
secret_key = "1aBcD3fGhIjKlMnOpQrStUvWxYz"

def generate_token(user: str, pwd: str):
    payload = {"user": user, "pwd": pwd}
    token = encode(payload, secret_key, algorithm="HS256")
    return token

def decode_token(token: str):
    payload = decode(token, secret_key, algorithms="HS256")
    username = payload["user"]
    return username