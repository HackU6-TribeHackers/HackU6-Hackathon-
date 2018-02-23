from django import forms

class Zip(forms.Form):
    zip = forms.CharField(label='zip', max_length=100)
