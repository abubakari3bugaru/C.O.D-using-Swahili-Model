from django import forms

class PredictionForm(forms.Form):
    # jina_kwanza = forms.CharField(max_length=100)
    # jina_pili = forms.CharField(max_length=100, required=False)
    # jina_mwisho = forms.CharField(max_length=100)
    # jinsia = forms.ChoiceField(choices=[('M', 'Mwanamume'), ('F', 'Mwanamke')])
    # ndoa = forms.BooleanField(required=False)
    # kuzaliwa = forms.DateField()
    # kufa = forms.DateField()
    # mahali = forms.CharField(max_length=100)
    # maelezo = forms.CharField(widget=forms.Textarea)
    sababu = forms.CharField(widget=forms.HiddenInput())

