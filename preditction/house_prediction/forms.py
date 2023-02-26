from django import forms
from .models import ModelPrediction


class PredictionForm(forms.ModelForm):
    class Meta:
        model = ModelPrediction
        fields = ['srf_de_vie', 'chambres', 'qual_global', 'qual_vue', 'adresse', 'vue_mer']
    
    QUAL_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13')
        
    )

    srf_de_vie = forms.IntegerField(label='Surface habitable',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surface de vie'}))
    chambres = forms.IntegerField(label='Nombres de chambres',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de chambres'}))
    qual_global = forms.ChoiceField(label='Qualité globale de la maison',choices=QUAL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    qual_vue = forms.ChoiceField(label='Qualité de la vue',choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], widget=forms.Select(attrs={'class': 'form-control'}))
    adresse = forms.CharField(label='Adresse',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}))
    vue_mer = forms.ChoiceField(choices=[(0, '0'), (1, '1')],widget=forms.Select(attrs={'class': 'form-check-input'}))


