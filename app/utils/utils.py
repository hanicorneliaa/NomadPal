import logging

def set_logging(log_level):
    logging.basicConfig(
        format="[%(asctime)s.%(msecs)03d][%(levelname)s][%(filename)s:%(funcName)s():%(lineno)d] %(message)s",
        level=log_level.upper(),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(__name__)
    return logger


class PromptSelector:
    def __init__(self):
        self.prompt = {
            "Student Tutor": "You are a math tutor.",
            "Travel Assistant": "You are a travel expert."
        }

    def get_use_cases(self):
        return self.prompt.keys()

    def get_system_prompt(self, use_case):
        if use_case is None:
            return ""
        return self.prompt.get(use_case)

