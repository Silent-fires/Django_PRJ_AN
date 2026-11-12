from django.db import models


class Prediction(models.Model):
    text = models.TextField()
    prediction = models.CharField(max_length=255)
    confidence = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.prediction} - {self.created_at}"
