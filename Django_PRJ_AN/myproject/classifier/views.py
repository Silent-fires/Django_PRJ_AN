import logging

from django.shortcuts import render
# from django.http import HttpResponse

from .forms import PredictionForm
from .models import Prediction
from myproject.ml.predict import TextClassifier

logger = logging.getLogger(__name__)


# 2a.1. Prediction Input View
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
        { "form": form, "result": result, },) 


# 2a.2. Prediction Results View
def display(request):
    try:
        entries = Prediction.objects.all()
        
        for entry in entries: # debuging
            print("")
            print(entry.id)
            print(entry.userInput)
            print(entry.prediction)
            print("")

        return render(request,"classifier/display.html",
            { "entries": entries, }) 
    
    except Exception as error:
        return render(request, "classifier/display.html",
            {"entries": [], "error": str(error)})
