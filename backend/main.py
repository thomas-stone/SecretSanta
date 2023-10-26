from mangum import Mangum
from fastapi import FastAPI
import boto3

from backend.routes.user_route import user_router

app = FastAPI()
client = boto3.client("dynamodb")

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_router, prefix="/user", tags=["user"])


handler = Mangum(app, lifespan="off")