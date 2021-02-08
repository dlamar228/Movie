from django import forms

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from . import constants

class UserAuthorizationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserAuthorizationForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({"class":"input-form",
                                                  "placeholder":"Enter your Login",
                                                  "autocomplete":"off",}
        )
        self.fields['password'].widget.attrs.update({'autocomplete': 'off',
                                                    "class":"input-form",
                                                    "placeholder":"Enter your Password",}
        )

    login = forms.CharField(
        label=('Login'),
        label_suffix="",
        max_length= constants.LOGIN_MAX_LENTH,
    )

    password = forms.CharField(
        label=("Password"),
        max_length= constants.PASSWORD_MAX_LENTH,
        strip=False,
        widget=forms.PasswordInput(),
    )

    def clean_login(self):
        text = self.cleaned_data['login']
        if len(text) < constants.LOGIN_MIN_LENTH:
            raise forms.ValidationError(constants.LOGIN_ERRORS["min"])
        elif len(text) > constants.LOGIN_MAX_LENTH:
            raise forms.ValidationError(constants.LOGIN_ERRORS["max"])
        return text

    def clean_password(self):
        text = self.cleaned_data['password']
        if len(text) < constants.PASSWORD_MIN_LENTH:
            raise forms.ValidationError(constants.PASSWORD_ERRORS["min"])
        elif len(text) > constants.PASSWORD_MAX_LENTH:
            raise forms.ValidationError(constants.PASSWORD_ERRORS["max"])
        return text

class UserRegistrtionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserRegistrtionForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({"class":"input-form",
                                                  "placeholder":"Enter your Email",
                                                  "autocomplete":"off",}
        )
        self.fields['login'].widget.attrs.update({"class":"input-form",
                                                  "placeholder":"Enter your Login",
                                                  "autocomplete":"off",}
        )
        self.fields['password_first'].widget.attrs.update({'autocomplete': 'off',
                                                            "class":"input-form",
                                                            "placeholder":"Enter your Password",
                                                            }
        )
        self.fields['password_second'].widget.attrs.update({'autocomplete': 'off',
                                                            "class":"input-form",
                                                            "placeholder":"Confirm your Password",
                                                            }
        )


    email = forms.EmailField(
        label=("Email"),
        label_suffix="",
        max_length= constants.EMAIL_MAX_LENTH,
    )

    login = forms.CharField(
        label=('Login'),
        label_suffix="",
        max_length= constants.LOGIN_MAX_LENTH,
    )

    password_first = forms.CharField(
        label=("Password"),
        label_suffix="",
        max_length= constants.PASSWORD_MAX_LENTH,
        strip=False,
        widget=forms.PasswordInput(),
    )

    password_second = forms.CharField(
        label=("Confirm Password "),
        label_suffix="",
        max_length= constants.PASSWORD_MAX_LENTH,
        strip=False,
        widget=forms.PasswordInput(),
    )

    def clean_password_first(self):
        text = self.cleaned_data['password_first']
        if len(text) < constants.PASSWORD_MIN_LENTH:
            raise forms.ValidationError(constants.PASSWORD_ERRORS["min"])
        elif len(text) > constants.PASSWORD_MAX_LENTH:
            raise forms.ValidationError(constants.PASSWORD_ERRORS["max"])
        return text

    def clean_password_second(self):
        text = self.cleaned_data['password_second']
        if len(text) < constants.PASSWORD_MIN_LENTH:
            raise forms.ValidationError(constants.PASSWORD_ERRORS["min"])
        elif len(text) > constants.PASSWORD_MAX_LENTH:
            raise forms.ValidationError(constants.PASSWORD_ERRORS["max"])
        return text

    def clean_email(self):
        text = self.cleaned_data['email']
        if len(text) < constants.EMAIL_MIN_LENTH:
            raise forms.ValidationError(constants.EMAIL_ERRORS["min"])
        elif len(text) > constants.EMAIL_MAX_LENTH:
            raise forms.ValidationError(constants.EMAIL_ERRORS["max"])
        elif len(User.objects.filter(email = text)) != 0 :
            raise forms.ValidationError(constants.EMAIL_ERRORS["registered"])
        return text

    def clean_login(self):
        text = self.cleaned_data['login']
        if len(text) < constants.LOGIN_MIN_LENTH:
            raise forms.ValidationError(constants.LOGIN_ERRORS["min"])
        elif len(text) > constants.LOGIN_MAX_LENTH:
            raise forms.ValidationError(constants.LOGIN_ERRORS["max"])
        elif len(User.objects.filter(username = text)) != 0 :
            raise forms.ValidationError(constants.LOGIN_ERRORS["registered"])
        return text

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("password_first")
        password2 = cleaned_data.get("password_second")

        if password1 != password2:
            self.add_error('password_second', constants.PASSWORD_ERRORS["equal"])

        return cleaned_data