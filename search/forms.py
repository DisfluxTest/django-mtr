from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(max_length=128, required=False)