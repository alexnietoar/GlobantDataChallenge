from fastapi import APIRouter, HTTPException
from api.security.tokens import generate_token

router = APIRouter()

@router.post("/login")
async def login(user: str, pwd: str):
    if user == "admin" and pwd == "admin":
        token = generate_token(user, pwd)
        print(token)
        return {"access_token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
