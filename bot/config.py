from typing import Optional
from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    bot_token: SecretStr
    admin_chat_id: int
    remove_sent_confirmation: bool = True

    database_url: PostgresDsn

    webhook_domain: Optional[str] = None
    webhook_path: Optional[str] = None
    app_host: str = "0.0.0.0"
    app_port: int = 9000
    custom_bot_api: Optional[str] = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

config = Settings()