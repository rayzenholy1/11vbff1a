import string
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

reviews = [
    "This phone is amazing, the battery lasts all day!",
    "The camera quality is great, but the price is too high.",
    "I love this phone, the screen is bright and the sound is clear.",
    "Delivery was fast, and the phone works perfectly.",
    "The battery is bad, it dies before the end of the day.",
    "Great phone for the price, the camera is really good.",
    "The screen is nice, but the phone is a bit heavy."
]

print("Вихідні відгуки:")
for r in reviews:
    print("-", r)

text = " ".join(reviews)
text = text.translate(str.maketrans("", "", string.punctuation))
text = text.lower()
print("\nОчищений текст:")
print(text)

tokens = word_tokenize(text)
print("\nЗагальна кількість токенів:", len(tokens))
print("Перші 10 токенів:", tokens[:10])

stop_words = set(stopwords.words("english"))
filtered = [w for w in tokens if w not in stop_words]
print("\nКількість токенів без стоп-слів:", len(filtered))
print("Токени без стоп-слів:", filtered)

freq = Counter(filtered)
print("\n10 найчастіших слів:")
for word, count in freq.most_common(10):
    print(f"{word}: {count}")
