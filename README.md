# Prédiction Maison
Version 1.0



## Description du Projet

Ce projet a été réalisé lors de la formation Tech IA chez Simplon HDF. L'objectif est de crée une application web contenant un modéle pour prédire des prix de maisons.
Le projet est directement lié [à ce projet**](https://github.com/ForskyOnly/ml_data_analyse_modelisation) et fais partie de la 4eme étape : l'implantation du modéle dans l'application.

**Cliquez pour en savoir plus sur les étapes précedantes : le nettoyage, la préparation et la modélisation.


### Contexte du projet


Nous sommes chargé de développer un algorithme qui pourra prédire le prix d’une maison en fonction d’autres paramètres, comme la surface en m², le nombre de chambres, etc.



## Organisation du dossier

Le dossier contient une fonctionallité principale nommé "house_prediction", dans ce dossier on retrouve plusieurs fichier et dossier : 
- Dossier "static" : Où se trouve tout les fichiers CSS utilisés pour les besoin du site;
- Dossier "templates" : Où se trouves toutes les pages HTML;
- Dossier "data" : Où se trouve notre modéle entrainé pour prédire le prix;
- Fichier "forms.py" : Contenant un exemple de formulaire afin de demander à l'utilisateur toutes les variables nécéssaire pour la prédiction du prix;
- Fichier "models.py": Contenant le Modéle de class crée pour sauvegarder toutes les estimations éffectuées sur le site;
- Fichier "views.py" : Contenant la vue, et la fonction principale pour l'application;
- Fichier "requirements.txt : Contenant la liste des dépendances Python nécessaires pour exécuter l'application.



## Utiliser l'application :  

### Pré-requis et installation:

- Pour utiliser le site il suffit de cloner le projet en [Cliquant Ici](https://github.com/ForskyOnly/djang_app_prediction) ;
- Avoir installé Python sur sa machine et avoir derniere version de Django;
- Se réfèrer au fichier "requirements.txt"