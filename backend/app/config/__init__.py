from pydantic_settings import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = "SecretSanta"
    DEBUG_MODE: bool = True
    API_V1_STR: str = "/api/v1"

class AuthSettings(BaseSettings):
    JWT_SECRET_KEY: str = "thisisasecretkey" ## store in .env file
    JWT_REFRESH_SECRET_KEY: str = "thisisarefreshsecretkey" ## store in .env file
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000

class DatabaseSettings(BaseSettings):
    DB_HOST: str = "http://dynamodb:8000" ### temp
    ENVIRONMENT: str = "test"
    AWS_REGION: str = "eu-west-1"

class Settings(CommonSettings, AuthSettings, ServerSettings, DatabaseSettings):
    pass

settings = Settings()