from django.shortcuts import render, redirect
from django.views import View
from app_orientation.forms import QuestionnaireForm, VotreFormulaire


class AccueilView(View):
    def get(self, request):
        page_active = '/'
        return render(request, 'index.html', {'page_active': page_active})


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


class PredictionView(View):
    def get(self, request):
        form = VotreFormulaire()
        return render(request, "pages/formulaire.html", {'form': form})

    def post(self, request):
        form = VotreFormulaire(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            predictions = VotreModele.predict([data['feature1'], data['feature2'], ...])
            return render(request, "resultat.html", {'predictions': predictions})
