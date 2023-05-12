from django import forms
from django.forms import ModelForm
from .models import Mhanga, Shuhuda, Uchunguzi


# class mhangaForm(ModelForm):
#     class Meta:
#         model = Mhanga
#         fields = '__all__'
    
class SubmitForm(forms.Form):
    firstName = forms.CharField(label='Jina La Mwanzo', max_length=100)
    middleName = forms.CharField(label='Jina La Kati', max_length=100)
    lastName = forms.CharField(label='Jina La Ukoo', max_length=100)
    place = forms.CharField(label='Mahali', max_length=100)
    region = forms.CharField(label='Mkoa', max_length=100)
    shahidi = forms.CharField(label='Shahidi', max_length=100)
    simu = forms.IntegerField(label='Simu')
    uhusiano_choices = [
        ('Baba', 'Baba'),
        ('Mama', 'Mama'),
        ('Ndugu', 'Ndugu'),
        ('Hakuna Uhusiano', 'Hakuna Uhusiano'),
        ('Nyingine', 'Nyingine'),
    ]
    uhusiano = forms.ChoiceField(label='Uhusiano na Marehemu', choices=uhusiano_choices)
    uhusiano_kipindi_kifo_choices = [
        ('Ndio', 'Ndio'),
        ('Hapana', 'Hapana'),
    ]
    uhusiano_kipindi_kifo = forms.ChoiceField(label='Uliishi na marehemu hadi kipindi amepoteza uhai?', choices=uhusiano_kipindi_kifo_choices)



class SubmitForm1(forms.Form):
    jina_kwanza = forms.CharField(label='Jina La Mwanzo', max_length=100)
    jina_pili = forms.CharField(label='Jina La Kati', max_length=100)
    jina_mwisho = forms.CharField(label='Jina La Mwisho', max_length=100)

    JINSIA_CHOICES = (
        ('mwanaume', 'Mwanaume'),
        ('mwanamke', 'Mwanamke'),
    )
    jinsia = forms.ChoiceField(label='Jinsia', choices=JINSIA_CHOICES, widget=forms.RadioSelect)

    HALI_NDOA_CHOICES = (
        ('ndoa', 'Ndoa'),
        ('hajafunga', 'Hajafunga Ndoa'),
        ('mjane', 'Mjane'),
        ('talaka', 'Talaka'),
        ('kutengana', 'Kutengana'),
        ('sijui', 'Sijui'),
    )
    ndoa = forms.ChoiceField(label='Hali Ya Ndoa', choices=HALI_NDOA_CHOICES, widget=forms.RadioSelect)

    kuzaliwa_year = forms.IntegerField(label='Marehemu Alizaliwa - Mwaka')
    kufa_year = forms.IntegerField(label='Marehemu Alikufa - Mwaka')
    MAHALI_KIFO_CHOICES = (
        ('Hospital', 'Hospital'),
        ('Nyumbani', 'Nyumbani'),
        ('Kituo Cha Afya', 'Kituo Cha Afya'),
        ('Sijui', 'Sijui'),
        ('Nyingine', 'Nyingine'),
    )
    mahali = forms.ChoiceField(label='Marehemu Alifariki', choices=MAHALI_KIFO_CHOICES, widget=forms.RadioSelect)

    maelezo = forms.CharField(label='Kuhusu Ugonjwa', widget=forms.Textarea(attrs={'rows': 4}))

    sababu1 = forms.CharField(label='Sababu 1 ya kifo kulingana na Mhojiwa', max_length=100)
    sababu2 = forms.CharField(label='Sababu 2 ya kifo kulingana na Mhojiwa', max_length=100)



# class SubmitForm1(forms.Form):
#     jina_kwanza = forms.CharField(label='Jina La Mwanzo')
#     jina_pili = forms.CharField(label='Jina La Kati')
#     jina_mwisho = forms.CharField(label='Jina La Mwisho')
#     jinsia = forms.CharField(label='Jinsia')
#     ndoa = forms.CharField(label='Hali Ya Ndoa')
#     kuzaliwa = forms.IntegerField(label='Marehemu  Alizaliwa')
#     kufa = forms.IntegerField(label='Marehemu  Alikufa')
#     mahali = forms.CharField(label='Marehemu Alifarikia')
#     maelezo = forms.CharField(label='Kuhusu Ugonjwa')
#     sababu1 = forms.CharField(label='Sababu 1 ya kifo kulinganga na Mhojiwa')
#     sababu2 = forms.CharField(label='Sababu 2 ya kifo kulinganga na Mhojiwa')



# class UchunguziForm(ModelForm):
#     class Meta:
#         model = Uchunguzi
#         fields = ['magonjwa', 'mengineyo']

class mhangaForm(ModelForm):
    class Meta:
        model = Mhanga
        fields = '__all__'
    
    
class UchunguziForm(forms.Form):
    firstName = forms.CharField(label='Jina La Mwanzo', max_length=100)
    middleName = forms.CharField(label='Jina La Kati', max_length=100)
    lastName = forms.CharField(label='Jina La Ukoo', max_length=100)
    place = forms.CharField(label='Mahali', max_length=100)
    region = forms.CharField(label='Mkoa', max_length=100)
    shahidi = forms.CharField(label='Shahidi', max_length=100)
    simu = forms.IntegerField(label='Simu')
    uhusiano_choices = [
        ('Baba', 'Baba'),
        ('Mama', 'Mama'),
        ('Ndugu', 'Ndugu'),
        ('Hakuna Uhusiano', 'Hakuna Uhusiano'),
        ('Nyingine', 'Nyingine'),
    ]
    uhusiano = forms.ChoiceField(label='Uhusiano na Marehemu', choices=uhusiano_choices)
    uhusiano_kipindi_kifo_choices = [
        ('Ndio', 'Ndio'),
        ('Hapana', 'Hapana'),
    ]
    uhusiano_kipindi_kifo = forms.ChoiceField(label='Uliishi na marehemu hadi kipindi amepoteza uhai?', choices=uhusiano_kipindi_kifo_choices)

 