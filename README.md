# NomadPal
Helping remote students in low-connectivity areas access personalized, AI-powered learning and Q&amp;A, completely offline, using a lightweight local language model and user-friendly interface.

![NomadPal: Self-hosted LLM](./gui.png)


## 🛠️ Tools Used

1. **[Ollama](https://ollama.com/)** / **[Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/llama)** – Local LLM model serving backend
2. **[Unsloth](https://github.com/unslothai/unsloth)** – LLM Model finetuning for specific tasks and domains
3. **[FastAPI](https://fastapi.tiangolo.com/)** – High-performance backend API framework for serving model inference
4. **[Gradio](https://gradio.app/)** – User-friendly graphical interface for interacting with the models
5. **Docker** [**Coming Soon**] – Containerization for simplified deployment and scalability
6. **Database** [**Coming Soon**] – Store and retrieve previous inference results for persistence

---

## 🚀 Features

- Serve LLMs locally using Ollama
- Model finetuned to adapt to specific tasks and domains using unsloth, trained on  **[mlabonne/FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k)** dataset
- API access to model responses via FastAPI
- Interactive UI for testing and experimentation using Gradio
- Modular design for easy extensions
- Docker support coming soon
- Database integration planned for saving/loading session history

---

## ⚙️ Installation

[**Coming Soon**]