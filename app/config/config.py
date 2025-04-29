
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    inference: str = "ollama"
    model_id: str = "llama3.2:1b"
    log_level: str = "DEBUG"
    llm_url: str = "http://localhost:11434"

    # fastapi
    fastapi_url: str = "http://localhost:8000/infer"

    # gradio
    gui_ip: str = "0.0.0.0"
    gui_port: int = 7860

class Request(BaseSettings):
    input: str
    use_case: Optional[str] = None
