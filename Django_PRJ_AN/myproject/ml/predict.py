
from pathlib import Path
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
        #prediction = ""
        confidence = None

        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba([text])[0]
            confidence = float(max(probabilities))

        # if (printRun == False):
        #     for val in self.label_names:
        #         print(val)
        #     printRun = True

        return {
            "text": text,
            "prediction": self.label_names[int(prediction)],
            "confidence": confidence,
        }


# Outside of TextClassifier
def predict(text):
    """
    Simple function that can be called from Django.
    """
    classifier = TextClassifier()
    return classifier.predict(text)
