# from fastapi import FastAPI
import logging

def set_logging(log_level):
    logging.basicConfig(
        format="[%(asctime)s.%(msecs)03d][%(levelname)s][%(filename)s:%(funcName)s():%(lineno)d] %(message)s",
        level=log_level.upper(),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(__name__)
    return logger

def get_system_prompt(use_case):
    if use_case == "Student Tutor":
        return "You are a math tutor."


from utils.ollama import LLMcaller
model_id = "mistral"
log_level = "DEBUG"
use_case = "Student Tutor"
localhost = "http://localhost:11434"
logger = set_logging(log_level)
system_prompt = get_system_prompt(use_case)

llm = LLMcaller(model_id, system_prompt, logger, localhost)
input = "Can you explain to me about pytaghoras theorem?"

llm.infer(input)