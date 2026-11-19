
from pathlib import Path
import sqlite3
import logging
import joblib

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "news_classifier.pkl"

class TextClassifier:
    """
    Machine learning classifier independent of Django.

    The classifier can be imported and tested directly from
    Python, Jupyter Notebook, or pytest.
    """

    def __init__(self, model_path=MODEL_PATH):
        self.model_path = Path(model_path)
        self.model = None
        self.label_names = None
        
    def load(self):
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        #self.model = joblib.load(self.model_path)
        self.model, self.label_names = joblib.load(MODEL_PATH)
        return self

    def predict(self, text):
        if self.model is None:
            self.load()

        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        prediction = self.model.predict([text])[0]
        result = self.label_names[int(prediction)]
        confidence = None

        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba([text])[0]
            confidence = float(max(probabilities))

        # if (printRun == False):
        #     for val in self.label_names:
        #         print(val)
        #     printRun = True

        print("")
        print(result)
        print("")

        addPrediction(text,result,confidence)

        return {
            "text": text,
            "prediction": result,
            "confidence": confidence,
        }


# Outside of TextClassifier
def predict(text):
    """
    Simple function that can be called from Django.
    """
    classifier = TextClassifier()
    return classifier.predict(text)

def addPrediction(userInput,prediction,confidence):
    # 1. Connect to the database (creates the file if it doesn't exist)
    with sqlite3.connect("../Django_PRJ_AN/db2.sqlite3") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ai_predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                userInput TEXT, 
                prediction TEXT, 
                confidence FLOAT)
            """)

        # 2. Define the SQL query with '?' placeholders to prevent SQL injection
        sql = "INSERT INTO ai_predictions (userInput, prediction, confidence) VALUES (?, ?, ?)"
        data = (userInput, prediction,confidence)
        addLog(f"Text: {userInput} - Predict: {prediction} - Confidence: {confidence}")

        # 3. Execute and save the entry
        cursor.execute(sql, data)
        conn.commit()

def addLog(logText):
    log_path = Path(__file__).resolve().parent.parent / "logs" / "predictions.log"

    # Create the 'logs' folder if it doesn't exist yet
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{logText}\n")

