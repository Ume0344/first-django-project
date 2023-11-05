from django import forms
from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "total_rooms",
            "location",
            "size",
            "image",
        ]
