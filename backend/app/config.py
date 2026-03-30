from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY:str = 'skibidi_sigma_rizzler'
    ALGORITH:str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 1440
    DATABASE_URL:str = 'sqlite:///./data/database.db'
    
    class Config:
        env_file = '.env'
        