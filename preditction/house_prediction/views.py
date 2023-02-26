import requests
import pickle
from django.shortcuts import render, redirect
from .forms import PredictionForm
from .models import ModelPrediction


with open('house_prediction/data/modele_knn.pkl', 'rb') as fichier:
    modele = pickle.load(fichier)
    
def prediction_prix(request):
    form = PredictionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            srf_de_vie = form.cleaned_data['srf_de_vie']
            chambres = form.cleaned_data['chambres']
            qual_global = form.cleaned_data['qual_global']
            qual_vue = form.cleaned_data['qual_vue']
            adresse = form.cleaned_data['adresse']
            vue_mer = form.cleaned_data['vue_mer']
            vue_mer_int = 1 if vue_mer else 0
            url = 'https://maps.googleapis.com/maps/api/geocode/json'
            params = {'address': adresse, 'key': 'AIzaSyCc0czRgbH_uyyw5W0zc6ieYfSUh2UqN78'}
            response = requests.get(url, params=params).json()
            if response['status'] == 'OK':
                lat = response['results'][0]['geometry']['location']['lat']
                long = response['results'][0]['geometry']['location']['lng']
            else:
                lat = 0.0
                long = 0.0
            prix_predit = modele.predict([[srf_de_vie, chambres, qual_global, qual_vue, lat, long, vue_mer]])
            modele_donnees = ModelPrediction(
                srf_de_vie=srf_de_vie,
                chambres=chambres,
                qual_global=qual_global,
                qual_vue=qual_vue,
                adresse=adresse,
                lat=lat,
                long=long,
                vue_mer=vue_mer,
                prix_predit=prix_predit[0])
            modele_donnees.save()
            return render(request, 'resultat.html', {'prix_predit': prix_predit[0]})
    return render(request, 'prediction.html', {'form': form})
