# train_news_classifier.py
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from pathlib import Path
import joblib

# Load data
data = fetch_20newsgroups(subset='train')
X, y = data.data, data.target

# Train pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('clf', LogisticRegression(max_iter=1000))
])
model.fit(X, y)

MODEL_PATH = Path(__file__).resolve().parent / "news_classifier.pkl"

# Save model + label names: file should exist already
joblib.dump((model, data.target_names), MODEL_PATH) #'news_classifier.pkl'
