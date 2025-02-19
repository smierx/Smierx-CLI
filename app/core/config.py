from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")
    VERSION_CONFIG: str #TODO Automatisiert

settings = Config()
