from django.shortcuts import render, redirect
from django.views import View
from app_orientation.forms import QuestionnaireForm, VotreFormulaire
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
import re
from .models import User
from .token import generatorToken


class AccueilView(View):
    def get(self, request):
        page_active = '/'
        return render(request, 'pages/utilpages/index.html', {'page_active': page_active})


class AboutView(View):
    def get(self, request):
        page_active = 'about'
        return render(request, "pages/front-pages/about.html", {'page_active': page_active})


class AptitudeView(View):
    def get(self, request):
        page_active = 'Tests d\'aptitude'
        return render(request, "pages/front-pages/aptitude.html", {'page_active': page_active})


class CompetancesView(View):
    def get(self, request):
        page_active = 'Evaluations de competances'
        return render(request, "pages/front-pages/competances.html", {'page_active': page_active})


class AssistanceView(View):
    def get(self, request):
        page_active = 'assistance'
        return render(request, "pages/front-pages/assistance.html", {'page_active': page_active})


class CommingSoonView(View):
    def get(self, request):
        page_active = 'commingsoon'
        return render(request, "pages/utilpages/comming_soon.html", {'page_active': page_active})


class OrientationView(View):
    def get(self, request):
        page_active = 'Services d\'orientation'
        return render(request, "pages/front-pages/orientation.html", {'page_active': page_active})


class ConseilsOrientationView(View):
    def get(self, request):
        page_active = 'Conseils d\'orientation'
        return render(request, "pages/front-pages/Conseils_orientation.html", {'page_active': page_active})


class ServicesView(View):
    def get(self, request):
        page_active = 'Services'
        return render(request, "pages/front-pages/services.html", {'page_active': page_active})


class PricingView(View):
    def get(self, request):
        page_active = 'pricing'
        return render(request, "pages/front-pages/pricing-page.html", {'page_active': page_active})


class CreerQuestionnaireView(View):
    def get(self, request):
        form = QuestionnaireForm()
        return render(request, "pages/creer_questionnaire.html", {'form': form})

    def post(self, request):
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultats')


def auth_register_cover(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')  # Récupérer la valeur du champ firstname
        lastname = request.POST.get('lastname')  # Récupérer la valeur du champ lastname

        try:
            # Vérifier si le nom d'utilisateur est déjà pris
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Le nom d\'utilisateur est déjà pris.')
                return redirect('auth_register_cover')

            # Vérifier si l'email est déjà associé à un compte
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Cet email est déjà associé à un compte.')
                return redirect('auth_register_cover')

            # Créer un nouvel utilisateur
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = firstname  # Définir la valeur du champ firstname
            user.last_name = lastname  # Définir la valeur du champ lastname
            user.is_active = False
            user.save()

            # Envoyer les e-mails de bienvenue et de confirmation ici

            messages.success(request, 'Votre compte a été créé avec succès.')
            return redirect('user_login')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('auth_register_cover')

    return render(request, 'pages/utilpages/auth-register-cover.html')


def user_login(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authentifier l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # L'utilisateur est authentifié.
            auth_login(request, user)
            firstname = user.first_name
            return render(request, 'pages/utilpages/index.html', {'firstname': firstname})
        else:
            # L'authentification a échoué.
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'pages/utilpages/auth-login-cover.html', {'error_message': error_message})

    return render(request, 'pages/utilpages/auth-login-cover.html')


class PredictionView(View):
    def get(self, request):
        form = VotreFormulaire()
        return render(request, "pages/front-pages/prediction-page.html", {'form': form})

    def post(self, request):
        form = VotreFormulaire(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            predictions = VotreModele.predict([data['feature1'], data['feature2'], ...])
            return render(request, "resultat.html", {'predictions': predictions})


class PsychotestView(View):
    def get(self, request):
        page_active = 'Psycho-test'
        return render(request, "pages/front-pages/Psychotest.html", {'page_active': page_active})
