from mangum import Mangum
from fastapi import FastAPI
import uvicorn
import boto3

from backend.routes.user_route import user_router
from backend.routes.group_route import group_router
from backend.routes.auth_route import auth_router

app = FastAPI()
client = boto3.client("dynamodb")

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(group_router, prefix="/group", tags=["group"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="localhost", port=8000, reload=True)