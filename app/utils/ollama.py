from ollama import Client
from utils.utils import PromptSelector

class LLMcaller:
    def __init__(self, model_id, logger, llm_url):

        self.model_id = model_id
        self.logger = logger
        self.llm_url = llm_url
        self.prompt_selector = PromptSelector()

        self.client = Client(host=self.llm_url)
        self.logger.info(f"Model `{self.model_id}` accessed from `{self.llm_url}`.")

    def infer(self, input, use_case):

        model_input = self._preprocess_input(input, use_case)
        self.logger.debug(f"input: {model_input}")
        response = self.client.chat(model=self.model_id, messages=model_input)
        output = self._postprocess_output(response)
        self.logger.debug(f"Output: {output}")
        return output


    def _preprocess_input(self, input, use_case):
        system_prompt = self.prompt_selector.get_system_prompt(use_case)
        messages = [
            {
                'role': "user",
                'content': f"{system_prompt} {input}",
            },
        ]
        return messages

    def _postprocess_output(self, output):
        output = output['message']['content']
        return output