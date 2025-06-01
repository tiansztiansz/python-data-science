from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    MODEL_PATH: str = "models/text_classification_model"
    API_USERNAME: str = "example_username"
    API_PASSWORD: str = "example_password"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    WORKERS: int = 1
    LOG_DIR: str = "logs"
    LOG_LEVEL: str = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOG_RETENTION_DAYS: int = 7
    MAX_RETRIES: int = 3  # 最大重启次数
    RESTART_DELAY: int = 5  # 重启延迟(秒)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
Path(settings.LOG_DIR).mkdir(parents=True, exist_ok=True)
