from django import forms


class BookImportForm(forms.Form):
    query = forms.CharField(label='Keyword',
                            max_length=100,
                            required=False)
