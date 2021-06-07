from django import forms
from django.core.exceptions import ValidationError

from dj1.models import Category


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        category = Category.objects.filter(name=name)
        if category:
            raise ValidationError("Такая котегория уже есть")
        return name
