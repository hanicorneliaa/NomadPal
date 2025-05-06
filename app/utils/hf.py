# need access for huggingface, use ollama instead if no access
from transformers import AutoModelForCausalLM, AutoTokenizer
from utils.utils import PromptSelector
import torch

class LLMcaller():
    def __init__(self, model_id, logger, max_new_tokens=1000, do_sample=True):

        self.model_id = model_id
        self.logger = logger
        self.max_new_tokens = max_new_tokens
        self.do_sample = do_sample
        self.prompt_selector = PromptSelector()

        self.model = AutoModelForCausalLM.from_pretrained(self.model_id,
                                                        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                                                        device_map="auto")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.logger.info(f"Model `{self.model_id}` loaded.")


    def infer(self, input, use_case):
        model_input = self._preprocess_input(input, use_case)
        generated_ids = self.model.generate(**model_input, max_new_tokens=self.max_new_tokens, do_sample=self.do_sample)
        output = self._postprocess_output(generated_ids)
        self.logger.debug(f"Output: {output}")
        return output


    def _preprocess_input(self, input, use_case):
        system_prompt = self.prompt_selector.get_system_prompt(use_case)
        self.full_prompt = f"{system_prompt} {input}. No extra details are necessary."
        encodeds = self.tokenizer(self.full_prompt, return_tensors="pt").to(self.model.device)
        return encodeds

    def _postprocess_output(self, output):
        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True)
        if decoded.startswith(self.full_prompt):
            decoded = decoded[len(self.full_prompt):].strip()
        return decoded


