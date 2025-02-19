from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")
    VERSION_CONFIG: str #TODO Automatisiert
    VERSION_VIEW: str #TODO Automatisiert

    BASE_PATH: str
    MODULE_PATH: str
    SUBMODULES_PATH: str

settings = Config()
