from ollama import Client

class LLMcaller:
    def __init__(self, model_id, system_prompt, logger, localhost):

        self.model_id = model_id
        self.system_prompt = system_prompt
        self.logger = logger
        self.localhost = localhost

        self.client = Client(host=localhost)
        self.logger.info(f"Model `{self.model_id}` accessed from `{localhost}`.")

    def infer(self, input):

        model_input = self._preprocess_input(input)
        self.logger.info(f"{model_input}")
        response = self.client.chat(model=self.model_id, messages=model_input)
        output = self._postprocess_output(response)
        self.logger.info(f"{output}")


    def _preprocess_input(self, input):
        messages = [
            {
                'role': "user",
                'content': f"{self.system_prompt} {input}",
            },
        ]
        return messages

    def _postprocess_output(self, output):
        output = output['message']['content']
        return output