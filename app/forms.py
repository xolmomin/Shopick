from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db.transaction import atomic
from django.forms import Form
from django import forms
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.models import Site



from app.models import User
from root.settings import EMAIL_HOST_USER
from app.views.token import account_activation_token



class RegistrationForm(Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    def clean_username(self):
        username = self.data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError(f"This username {username} already taken")
        return username

    def clean_email(self):
        email = self.data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError(f"This email {email} already taken")

        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Passwords do not match")

        return password

    @atomic
    def save(self):
        user = User.objects.create_user(
            first_name=self.data.get('first_name'),
            last_name=self.data.get('last_name'),
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            is_active=False,
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

    def clean_password(self):
        username = self.data.get('username')
        password = self.data.get('password')

        user = User.objects.filter(username=username).first()
        if user and not user.check_password(password):
            return ValidationError('Password entered error')
        return password

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class ForgotPasswordForm(Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("This profile not registered")
        return email


class UserModelForm:
    class Meta:
        model = User
        exclude = ()


def send_email(email, request, _type):

    user = User.objects.get(email=email)
    subject = 'Activate your account'
    current_site = get_current_site(request)
    message = render_to_string('app/auth/activation_account.html', {
        'user': user,
        'domain': current_site.name,
        'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
        'token': account_activation_token.make_token(user),
    })

    from_email = EMAIL_HOST_USER
    recipient_list = [email]

    result = send_mail(subject, message, from_email, recipient_list)
    print('Send to MAIL')
