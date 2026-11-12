import logging

from django.shortcuts import render
# from django.http import HttpResponse

from .forms import PredictionForm
from .models import Prediction
from myproject.ml.predict import TextClassifier

logger = logging.getLogger(__name__)


# def classify(request):
#     return HttpResponse("ML Classifier is working!")

def classify(request):
    result = None

    if request.method == "POST":
        form = PredictionForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data["text"]

            try:
                classifier = TextClassifier()
                result = classifier.predict(text)
            except Exception as error:
                result = {"error": str(error)}
    else:
        form = PredictionForm()

    return render(request,"classifier/results.html",
        { "form": form, "result": result, },
    )

#region old
# def classify_text(request):
#     result = None

#     if request.method == "POST":
#         form = PredictionForm(request.POST)

#         if form.is_valid():
#             text = form.cleaned_data["text"]

#             try:
#                 result = predict(text)

#                 Prediction.objects.create(
#                     text=text,
#                     prediction=result["prediction"],
#                     confidence=result["confidence"],
#                 )

#                 logger.info(
#                     "Prediction made: prediction=%s confidence=%s",
#                     result["prediction"],
#                     result["confidence"],
#                 )

#             except Exception:
#                 logger.exception("Prediction failed.")

#                 result = {
#                     "error": "Unable to make prediction."
#                 }

#     else:
#         form = PredictionForm()

#     return render(request,"classifier/results.html",
#         { "form": form, "result": result, },
#     )
#endregion