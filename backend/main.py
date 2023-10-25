from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{username}")
async def get_user(username):
    return {"message": f"Hello {username}"}


@app.post("/user/{username}")
async def root(username):
    return {"message": f"POSTING {username}"}


@app.get("/idk")
async def root():
    return {"message": "Hello World"}


handler = Mangum(app, lifespan="off")