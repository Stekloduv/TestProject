import os
import re
import pandas as pd
from transcriber import transcribe_audio
from analyzer import analyze_text

AUDIO_DIR = "audio"
TRANSCRIPTS_DIR = "transcripts"
RESULTS_FILE = "results.csv"


def extract_datetime_from_filename(filename):
    """
    Витягує дату та час із назви файлу у форматі YYYY-MM-DD HH:MM.
    Наприклад: 2024-11-13_10-09_0933608802_incoming.mp3 -> 2024-11-13 10:09
    """
    match = re.search(r'(\d{4}-\d{2}-\d{2})_(\d{2})-(\d{2})', filename)
    if match:
        date_part = match.group(1)
        hour = match.group(2)
        minute = match.group(3)
        return f"{date_part} {hour}:{minute}"
    return None


def main():
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

    results = []

    for filename in os.listdir(AUDIO_DIR):
        if filename.endswith((".mp3", ".wav")):
            audio_path = os.path.join(AUDIO_DIR, filename)
            transcript_path = os.path.join(TRANSCRIPTS_DIR, filename + ".txt")

            print(f"\n🎧 Обробка файлу: {filename}")
            text = transcribe_audio(audio_path)

            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(text)

            rating, comment, found_work = analyze_text(text)

            print(f"Рейтинг: {rating}, Коментар: {comment}")
            print(f"Знайдені роботи: {found_work}")

            datetime_str = extract_datetime_from_filename(filename)

            results.append({
                "file_name": filename,
                "transcript_path": transcript_path,
                "datetime": datetime_str,
                "rating": rating,
                "comment": comment,
                "found_work": ", ".join(found_work)
            })

    df = pd.DataFrame(results)
    df.to_csv(RESULTS_FILE, index=False, encoding="utf-8-sig")
    print("\n✅ Готово! Результати збережено у results.csv")


if __name__ == "__main__":
    main()