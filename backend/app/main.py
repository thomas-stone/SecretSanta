from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Allow cookies to be included in the requests
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.APP_NAME,
        version="0.0.1",
        description="OpenAPI Schema for SecretSanta API",
        routes=app.routes,
    )
    openapi_schema["servers"]= [
        {
            "url": f"http://{settings.HOST}:{settings.PORT}"
        }
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

@app.get("/", tags=["ping"])
def ping():
    return {"message:": f"Server is working, go to http://{settings.HOST}:{settings.PORT}/docs for api docs"}

app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG_MODE)