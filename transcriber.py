import whisper
import torch

# Вибір пристрою
device = "cuda" if torch.cuda.is_available() else "cpu"

# Завантажуємо модель один раз
model = whisper.load_model("medium").to(device)


def transcribe_audio(file_path, model=model, device=device):
    """
    Транскрибує аудіо файл, автоматично на GPU якщо доступно.
    """
    result = model.transcribe(file_path, language="uk")
    return result["text"]
