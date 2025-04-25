# need access for huggingface, use ollama instead if no access
from transformers import AutoModelForCausalLM, AutoTokenizer

class LLMcaller():
    def __init__(self, model_id, system_prompt, logger, max_new_tokens=1000, do_sample=True):

        self.model_id = model_id
        self.system_prompt = system_prompt
        self.logger = logger
        self.max_new_tokens = max_new_tokens
        self.do_sample = do_sample

        self.model = AutoModelForCausalLM.from_pretrained(self.model_id)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.logger.info(f"Model `{self.model_id}` loaded.")


    def infer(self, input):

        model_input = self._preprocess_input(input)
        generated_ids = self.model.generate(model_input, max_new_tokens=1000, do_sample=True)
        output = self._postprocess_output(generated_ids)
        self.logger.info(f"{output}")


    def _preprocess_input(self, input):
        messages = [
            {"role": "user", "content": f"{self.system_prompt} \n{input}"}
        ]
        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
        return encodeds

    def _postprocess_output(self, output):
        decoded = self.tokenizer.batch_decode(output)
        return decoded


