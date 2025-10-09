import re
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def analyze_text(text):
    bad_phrases = [
        "не знаю", "чекайте", "мені байдуже", "що ви хочете", "не можу допомогти"
    ]

    issues = [phrase for phrase in bad_phrases if phrase.lower() in text.lower()]

    # Аналіз тону
    result = sentiment_model(text[:512])[0]  # обмежуємо довжину для швидкості
    sentiment = result['label']

    # Проста оцінка 0–10
    rating = 10
    if sentiment.lower().startswith("negative"):
        rating -= 3
    if issues:
        rating -= len(issues)

    comment = "✅ Все добре" if rating > 7 else f"❌ Проблеми: {', '.join(issues)}"
    if issues:
        comment = f"\033[91m{comment}\033[0m"  # червоний текст у терміналі

    return sentiment, max(rating, 0), comment