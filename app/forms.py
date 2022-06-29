from django.core.exceptions import ValidationError
from django.db.transaction import atomic
from django.forms import Form
from django import forms

from app.models import User


class RegistrationForm(Form):
    username = forms.CharField()
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

    def clean_username(self):
        username = self.data.get('username')

        if not User.objects.filter(username=username).exists():
            raise ValidationError("This username already taken")

        return username

    def clean_email(self):
        email = self.data.get('email')

        if not User.objects.filter('email').exists():
            raise ValidationError("This email already taken")

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
            username=self.cleaned_data.get('username'),
            email=self.cleaned_data.get('email'),
            is_active=False,

        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()


class UserModelForm:
    class Meta:
        exclude = ()

