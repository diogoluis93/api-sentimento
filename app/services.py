import re
from collections import Counter
from transformers import pipeline
from .cache import store_result
from .models import TextInput

stopwords = {"e", "de", "o", "a", "que", "do", "da", "em", "um", "para", "é"}

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def analyze_text_service(input: TextInput) -> dict:
    text = input.text.lower()
    words = re.findall(r'\b\w+\b', text)
    filtered_words = [w for w in words if w not in stopwords]

    word_count = len(words)
    most_common = Counter(filtered_words).most_common(5)

    sentiment_result = sentiment_pipeline(input.text)
    sentiment = sentiment_result[0]['label'].lower()

    result = {
        "word_count": word_count,
        "top_words": most_common,
        "sentiment": sentiment
    }

    store_result(input.text, result)
    return result