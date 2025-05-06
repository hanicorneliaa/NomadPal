# Training


## Training Information

1. Llama-3.2-1B model trained using **[Unsloth](https://github.com/unslothai/unsloth)** on **[mlabonne/FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k)** dataset.
2. Model trained using T4 GPU Cuda 12.5 on Google Colab.
3. Training parameters include:
 * Batch size: 2
 * Gradient accumulation steps: 4
 * Warmup steps: 5
 * Max steps: 60
 * Learning rate: 2e-4
4. Model is saved to gguf format after training, with 8bit quantization for balanced trade-off between inference speed and accuracy.
5. Then it is converted to ollama format to be served using ollama.
```ollama create llama-3-2-1b:finetuned-finetome-100k -f Modelfile```