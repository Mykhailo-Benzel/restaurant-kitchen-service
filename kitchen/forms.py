from django import forms

from kitchen.models import DishType


class DishTypeForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter the type of dish here"})
    )

    class Meta:
        model = DishType
        fields = "__all__"
