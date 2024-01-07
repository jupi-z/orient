from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import QuestionnaireForm
from .forms import VotreFormulaire


def accueil(request):
    page_active = '/'
    return render(request, 'index.html', {'page_active': page_active})


def about(request):
    page_active = 'about'
    return render(request, "pages/about.html", {'page_active': page_active})


def contact(request):
    page_active = 'contact'
    return render(request, "pages/contact.html", {'page_active': page_active})


def cursus(request):
    page_active = 'cursus'
    return render(request, "pages/cursus.html", {'page_active': page_active})


def filiere(request):
    page_active = 'filiere'
    return render(request, "pages/filiere.html", {'page_active': page_active})


def test(request):
    page_active = 'cursus'
    return render(request, "pages/test.html", {'page_active': page_active})


def creer_questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultats')
    else:
        form = QuestionnaireForm()

    return render(request, "pages/creer_questionnaire.html", {'form': form})


def prediction_view(request):
    if request.method == 'POST':
        form = VotreFormulaire(request.POST)
        if form.is_valid():
            # Récupérez les données du formulaire
            data = form.cleaned_data
            # Effectuez les prédictions en utilisant votre modèle
            predictions = VotreModele.predict([data['feature1'], data['feature2'], ...])
            # Envoyez les prédictions au template
            return render(request, "resultat.html", {'predictions': predictions})
    else:
        form = VotreFormulaire()

    return render(request, "pages/formulaire.html", {'form': form})
