from products import forms
from django.forms import ModelForm
from products.models import product


class productform(forms.ModelForm):
    class Meta:
        model = product
        fields = [
            'title',
            'description',
            'price'
        ]
