
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    inference: str = "ollama"
    model_id: str = "mistral"
    log_level: str = "DEBUG"
    use_case: str = "Student Tutor"
