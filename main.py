import os
import pandas as pd
from transcriber import transcribe_audio
from analyzer import analyze_text

AUDIO_DIR = "audio"
TRANSCRIPTS_DIR = "transcripts"
RESULTS_FILE = "results.csv"


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

            sentiment, rating, comment = analyze_text(text)

            results.append({
                "file_name": filename,
                "transcript_path": transcript_path,
                "sentiment": sentiment,
                "rating": rating,
                "comment": comment
            })

    df = pd.DataFrame(results)
    df.to_csv(RESULTS_FILE, index=False, encoding="utf-8-sig")
    print("\n✅ Готово! Результати збережено у results.csv")


if __name__ == "__main__":
    main()
