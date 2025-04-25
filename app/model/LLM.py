from transformers import AutoModelForCausalLM, AutoTokenizer
import logging


class LLMwrapper():
    def __init__(self, model_id, max_new_tokens=1000, do_sample=True):

        self.model_id = model_id
        self.max_new_tokens = max_new_tokens
        self.do_sample = do_sample

        self.model = AutoModelForCausalLM.from_pretrained(self.model_id)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)


    def infer(self):

        model_inputs =
        self.model.generate(model_inputs, max_new_tokens=1000, do_sample=True)