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
    VUE_MER = (
        (0,'non'),
        (1,'oui')
    )
    
    QUAL_VUE = (
        (0,'Vue correct'),
        (1,'Vue normale'),
        (2,'Belle vue'),
        (3,'Trés belle vue'),
        (4,'Vue exceptionnel')
    )

    srf_de_vie = forms.IntegerField(label='Surface habitable en sqft', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Espace de vie intérieur'}))
    chambres = forms.IntegerField(label='Nombres de chambres', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de chambres'}))
    qual_global = forms.ChoiceField(label='Qualité globale de la maison', choices=QUAL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    qual_vue = forms.ChoiceField(label='Qualité de la vue', choices=QUAL_VUE, widget=forms.Select(attrs={'class': 'form-control'}))
    adresse = forms.CharField(label='Adresse', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}))
    vue_mer = forms.ChoiceField(choices=VUE_MER, widget=forms.Select(attrs={'class': 'form-check-input'}))


