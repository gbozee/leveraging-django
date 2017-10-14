
from django import forms
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(email)s and password."
        ),
    }

    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request=request, *args, **kwargs)
        # we are not interested in the username field so we would set it as not
        # required
        self.fields['username'].required = False

    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'email': "Email"},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

