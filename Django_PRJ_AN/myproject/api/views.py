from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ml.predict import predict


@api_view(["POST"])
def predict_api(request):
    text = request.data.get("text")

    if not text:
        return Response(
            {"error": "text is required"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        result = predict(text)

        return Response(result)

    except Exception as exc:
        return Response(
            {"error": str(exc)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
