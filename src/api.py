from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.encoders import jsonable_encoder
from db.queries import get_db_connection, get_task1, get_task2
from jwt import encode, decode
import uvicorn

app = FastAPI()
conn = get_db_connection()
security = HTTPBearer()

data_types = {
    'hired_employees': {
        'id': int,
        'name': str,
        'datetime': str,
        'department_id': int,
        'job_id': int
    },
    'departments': {
        'id': int,
        'department': str
    },
    'jobs': {
        'id': int,
        'job': str
    }
}

def generate_token(username: str, password: str):
    secret_key = "1aBcD3fGhIjKlMnOpQrStUvWxYz"
    payload = {"username": username, "password": password}
    token = encode(payload, secret_key, algorithm="HS256")
    return token

@app.get("/task1")
def task1(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        secret_key = "1aBcD3fGhIjKlMnOpQrStUvWxYz"
        payload = decode(token, secret_key, algorithms=["HS256"])
        username = payload["username"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    results = get_task1()
    return jsonable_encoder(results)


@app.get("/task2")
def task2(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        secret_key = "1aBcD3fGhIjKlMnOpQrStUvWxYz"
        payload = decode(token, secret_key, algorithms=["HS256"])
        username = payload["username"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    results = get_task2()
    return jsonable_encoder(results)

@app.post("/login")
async def login(username: str, password: str):
    if username == "admin" and password == "admin":
        token = generate_token(username, password)
        return {"access_token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/insert/{table_name}")
async def insert_data(table_name: str, data: dict, credentials: HTTPAuthorizationCredentials = Depends(security)):

    try:
        token = credentials.credentials
        secret_key = "1aBcD3fGhIjKlMnOpQrStUvWxYz"
        payload = decode(token, secret_key, algorithms=["HS256"])
        username = payload["username"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

    schema = data_types.get(table_name)

    if not schema:
        raise ValueError(f"Table {table_name} not found in data_types.")

    if set(data.keys()) != set(schema.keys()):
        raise ValueError(f"The provided data does not match the schema for {table_name} table.")

    for key, value in data.items():
        if not isinstance(value, schema[key]):
            raise ValueError(f"The provided value for {key} does not match the expected type {schema[key]}.")

    cur = conn.cursor()
    keys = ', '.join(data.keys())
    values = tuple(data.values())
    placeholders = ', '.join('?' * len(data))
    query = f"INSERT INTO {table_name} ({keys}) VALUES ({placeholders})"
    cur.execute(query, values)
    conn.commit()
    return {"message": f"{cur.rowcount} row(s) inserted into {table_name} table."}



def main():
    print("Está escuchando")
    uvicorn.run(app, host="0.0.0.0", port=8000)
