from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.context_processors import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView, FormView
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app.views.token import account_activation_token
from app.forms import send_email
from django.contrib import messages

from app.forms import ForgotPasswordForm


class LoginPage(LoginView):
    form_class = LoginForm
    template_name = 'app/auth/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)


class RegisterPage(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'app/auth/register.html'

    def form_valid(self, form):
        form.save()
        send_email(form.data.get('email'), self.request, 'register')
        messages.add_message(
            self.request,
            level=messages.WARNING,
            message='Successfully send your email, Please activate your profile'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogoutPage(LogoutView):
    success_url = reverse_lazy('index')


class ForgotPasswordPage(FormView):
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('login')
    template_name = 'app/auth/forgot_password.html'

    def form_valid(self, form):
        send_email(form.data.get('email'), self.request, 'forgot')
        return super().form_valid(form)


class ActivateEmailView(TemplateView):
    template_name = 'app/auth/activation_account.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uuid')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print(e)
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Your account successfully activated!"
            )
            return redirect('index')
        else:
            return HttpResponse('Activation link is invalid!')


class MyAccPage(TemplateView):
    template_name = 'app/auth/my-account.html'
