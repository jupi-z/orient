from authentification import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
import re
from .models import User
from .token import generatorToken


def home(request):
    return render(request, 'app/index.html')


def register(request):
    if request.method == "POST":
        # Récupérer les données du formulaire
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Vérifier si les mots de passe correspondent
        if password != password_confirm:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return redirect('register')

        # Vérifier si le nom d'utilisateur contient uniquement des caractères alphanumériques
        if not username.isalnum():
            messages.error(request, 'Le nom d\'utilisateur ne doit contenir que des caractères alphanumériques.')
            return redirect('register')

        # Vérifier si le nom d'utilisateur est déjà pris
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Le nom d\'utilisateur est déjà pris.')
            return redirect('register')

        # Vérifier si l'email est déjà associé à un compte
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà associé à un compte.')
            return redirect('register')



        try:
            # Créer un nouvel utilisateur
            user = User.objects.create_user(username=username, email=email, password=password)
            user.firstname = firstname
            user.lastname = lastname
            user.is_active = False
            user.save()

            messages.success(request, 'Votre compte a été créé avec succès.')
            # ENVOI D'email de bienvenue
            subject = "Bienvenue sur Ruth"
            message = "Bienvenue " + user.firstname + " " + user.lastname + " !\nNous sommes heureux de vous compter " \
                                                                            "parmi nous.\n\nMerci.\n"
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            # Email de confirmation
            current_site = get_current_site(request)
            email_subject = "Confirmation de l'adresse email sur Ruth"
            messageConfirm = render_to_string("emailConfirm.html", {
                "name": user.firstname,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generatorToken.make_token(user)
            })

            email = EmailMessage(
                email_subject,
                messageConfirm,
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            email.fail_silently = False
            email.send()

            return redirect('user_login')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('register')

    return render(request, 'app/register.html')




def logout_view(request):
    logout(request)
    return render(request, 'app/auth-login-cover.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Votre compte a été activé. Connectez-vous maintenant.")
        return redirect('user_login')
    else:
        messages.error(request, 'L\'activation a échoué. Réessayez plus tard.')
        return redirect('home')
