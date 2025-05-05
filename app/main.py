from fastapi import FastAPI
from fastapi import BackgroundTasks
from contextlib import asynccontextmanager
from config.config import Settings, Request
from utils.utils import set_logging


settings = Settings()
logger = set_logging(settings.log_level)

async def init_llm(app: FastAPI):
    logger.info("Start llm api")
    if settings.inference == "ollama":
        from utils.ollama import LLMcaller
        app.state.llm = LLMcaller(settings.model_id, logger, settings.llm_url)
    elif settings.inference == "huggingface":
        from utils.hf import LLMcaller
        app.state.llm = LLMcaller(settings.model_id, logger)
    else:
        raise Exception("Inference backend not supported")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("App starting up")
    await init_llm(app)
    # add more functionalities here later, ie database etc
    yield
    logger.info("App shutting down")
    # clear up gracefully later

app = FastAPI(lifespan=lifespan)

@app.post(f"/infer")
async def run_inference(request: Request):
    try:
        result = app.state.llm.infer(request.input, request.use_case)
        return result
    except Exception as e:
        logger.error(f"Error during inference: {str(e)}")
        return "Error during inference"