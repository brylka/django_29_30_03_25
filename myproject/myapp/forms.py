from django import forms


class LinearEquationForm(forms.Form):
    a = forms.FloatField(label="Współczynnik a")
    b = forms.FloatField(label="Współczynnik b")
