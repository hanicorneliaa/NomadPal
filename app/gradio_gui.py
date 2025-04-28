import gradio as gr
import requests
from config.config import Settings
from utils.utils import PromptSelector

settings = Settings()
prompt_selector = PromptSelector()

def infer_fn(use_case, input):
    response = requests.post(f"{settings.fastapi_url}", json={"input": input, "use_case": use_case})
    result = response.json()
    return result

def start_gradio(infer_fn, gui_ip, gui_port):
    dropdown_choices = prompt_selector.get_use_cases()
    interface = gr.Interface(
        fn=infer_fn,
        inputs=[
            gr.Dropdown(choices=dropdown_choices, label="Who do you want to talk to?", multiselect=False),
            gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
        ],
        outputs="text",
        title="NomadPal",
        description="Input a prompt and get a response from the model."
    )
    interface.launch(share=False, server_name=gui_ip, server_port=gui_port)


def main():
    start_gradio(infer_fn, settings.gui_ip, settings.gui_port)

if __name__ == '__main__':
    main()