from django import forms
from .models import ModelPrediction


class PredictionForm(forms.ModelForm):
    class Meta:
        model = ModelPrediction
        fields = ['srf_de_vie', 'chambres', 'qual_global', 'qual_vue', 'adresse', 'vue_mer','sd_bain']
    
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
        (0,'Sans vue'),
        (1,'Vue limitée'),
        (2,'Vue partielle'),
        (3,'Vue degagée'),
        (4,'Vue Panoramique')
    )
    
    SD_BAIN = (
        (0.00, '0'),
        (0.50, '0.5'),
        (0.75, '0.75'),
        (1.00, '1'),
        (1.25, '1.25'),
        (1.50, '1.50'),
        (1.75, '1.75'),
        (2.00, '2'),
        (2.50, '2.5'),
        (2.75, '2.75'),
        (3.00, '3'),
        (3.25, '3.25'),
        (3.50, '3.5'),
        (3.75, '3.75'),
        (4.00, '4'),
        (4.25, '4.25'),
        (4.50, '4.5'),
        (4.75, '4.75'),
        (5.00, '5'),
        (5.25,' 5.25'),
        (5.50, '5.5'),
        (5.75, '5.75'),
        (6.00, '6'),
        (6.25, '6.25'),
        (6.50, '6.5'),
        (6.75, '6.75'),
        (7.00, '7'),
        (7.25, '7.25'),
        (7.50, '7.5'),
        (7.75, '7.75'),
        (8.00, 'autre')
        

    )

    srf_de_vie = forms.IntegerField(label='Surface habitable en sqft', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Espace de vie intérieur'}))
    sd_bain = forms.ChoiceField(label='Salles de bain', choices=SD_BAIN, widget=forms.Select(attrs={'class': 'form-check-input'}))
    chambres = forms.IntegerField(label='Nombres de chambres', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de chambres'}))
    qual_global = forms.ChoiceField(
        label='Qualité globale de la maison',
        choices=QUAL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="<p class='qual_help'> <span>Une mesure</span> de la qualité globale de la maison en prenant en compte la qualité de contrsutciotn, le disigne, la qualité des matérieux etc.</p>"
        )
    qual_vue = forms.ChoiceField(
        label='Qualité de la vue',
        choices=QUAL_VUE,
        widget=forms.Select(attrs={'class': 'hovqual_vue', 'id': 'qual_vue'}),
        help_text="<p class='qual_vue_help'><span>Sans vue: </span> Une maison qui n'a pas de vue particulière et qui est entourée d'autres maisons ou de bâtiments.<br><span>Vue limitée :</span> Une vue qui est limitée ou obstruée par des bâtiments ou des arbres, et qui offre une vue partielle ou limitée des environs.<br><span>Vue partielle</span> : Une vue qui est partiellement obstruée par des bâtiments ou des arbres, mais qui offre néanmoins une vue sur les environs.<br><span>Vue dégagée :</span> Une vue qui n'est pas obstruée par des bâtiments ou des arbres, et qui offre une vue dégagée sur les environs.<br><span>Vue panoramique :</span> Une vue qui offre une vue panoramique à 180 degrés sur les environs, offrant une vue large et ouverte.</p>")
    adresse = forms.CharField(
        label='Adresse',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
        help_text="<p class='adresse_help'> <span>Veuillez préciser </span> l'adresse complet de la maison avec : la rue, le numero, la ville et le code postale. </p>")
    
    vue_mer = forms.ChoiceField(label='Vue sur mer', choices=VUE_MER, widget=forms.Select(attrs={'class': 'form-check-input'}))
    
    


