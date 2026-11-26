from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from myproject.ml.predict import predict
from django.http import JsonResponse


@api_view(["GET", "POST"])
def predict_api(request): # To use: ?text=
    text = request.data.get("text") or request.query_params.get("text")

    if not text:
        return JsonResponse(
            {"error": "text is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        result = predict(text)

        return JsonResponse(result)

    except Exception as exc:
        return JsonResponse(
            {"error": str(exc)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
