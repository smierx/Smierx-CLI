from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")
    BASE_PATH: str
    ZETTEL_REL_PATH: str
    LECTURE_REL_PATH: str
    LECTURE_METADATA: str
    LECTURE_METADATA_STR: str
    TEMPLATE_REL_PATH: str
    TEMPLATE_CSV: str
    TABLES_REL_PATH: str
    START_ROW: int = 4

settings = Config()
