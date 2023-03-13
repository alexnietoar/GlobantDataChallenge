from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from db.queries import get_db_connection, get_task1
from ..security.tokens import security, credential, decode_token
import jwt

router = APIRouter()
conn = get_db_connection()

@router.get("/task1")
def get_task1(credentials: str = Depends(security) ):
    try:
        token = credentials.credentials
        username = decode_token(token)
    except jwt.exceptions.DecodeError as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid token")
    
    results = get_task1()
    return jsonable_encoder(results)
