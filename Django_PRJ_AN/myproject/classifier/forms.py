from django import forms


class PredictionForm(forms.Form):
    text = forms.CharField(
        label="Enter text",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Enter text to classify...",
            }
        ),
        max_length=5000,
    )
