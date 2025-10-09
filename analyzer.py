def analyze_text(text):
    """
    Перевіряє текст на наявність небажаних фраз.
    Повертає rating та comment.
    """

    bad_phrases = [
        "не знаю", "чекайте", "мені байдуже", "що ви хочете", "не можу допомогти"
    ]

    issues = [phrase for phrase in bad_phrases if phrase.lower() in text.lower()]

    # Проста оцінка 0–10
    rating = 10
    if issues:
        rating -= len(issues)

    comment = "✅ Все добре" if rating > 7 else f"❌ Проблеми: {', '.join(issues)}"
    if issues:
        comment = f"\033[91m{comment}\033[0m"

    return rating, comment