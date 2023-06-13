from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Arama', max_length=100)