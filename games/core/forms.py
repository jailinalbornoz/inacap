from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows":4}),
            "precio": forms.NumberInput(attrs={"step": "0.01"}),
            "stock": forms.NumberInput(),
        }
