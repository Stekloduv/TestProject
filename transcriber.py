import whisper


def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path, language="uk")
    return result["text"]
