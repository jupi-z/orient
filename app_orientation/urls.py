from django.urls import path
from . import views
from app_orientation.views import (
    AccueilView,
    AboutView,
    AptitudeView,
    CompetancesView,
    AssistanceView,
    OrientationView,
    ConseilsOrientationView,
    CreerQuestionnaireView,
    PredictionView,
    ServicesView,
    PricingView,
    CommingSoonView,
    user_login,
    auth_register_cover,
    PsychotestView,

)

urlpatterns = [
    path('', AccueilView.as_view(), name='accueil'),
    path('about/', AboutView.as_view(), name='about'),
    path('aptitude/', AptitudeView.as_view(), name='aptitude'),
    path('competances/', CompetancesView.as_view(), name='competances'),
    path('assistance/', AssistanceView.as_view(), name='assistance'),
    path('orientation/', OrientationView.as_view(), name='orientation'),
    path('conseils_orientation/', ConseilsOrientationView.as_view(), name='conseils_orientation'),
    path('creer_questionnaire/', CreerQuestionnaireView.as_view(), name='creer_questionnaire'),
    path('prediction/', PredictionView.as_view(), name='prediction'),
    path('services/', ServicesView.as_view(), name='services'),

    path('pricing/', PricingView.as_view(), name='pricing'),
    path('Psychotest/', PsychotestView.as_view(), name='Psychotest'),
    path('comming_soon/', CommingSoonView.as_view(), name='comming_soon'),
    path('user_login/', user_login, name='user_login'),
    path('auth-register-cover/', views.auth_register_cover, name='auth_register_cover'),

]
