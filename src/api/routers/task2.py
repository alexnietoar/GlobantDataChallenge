from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from db.queries import get_db_connection, get_task2
from ..security.tokens import security, credential, decode_token

router = APIRouter()
conn = get_db_connection()

@router.get("/task2")
def get_task2(credentials: credential = Depends(security)):
    try:
        token = credentials
        username = decode_token(token)
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    results = get_task2()
    return jsonable_encoder(results)
