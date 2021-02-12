from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect

from django.views.generic.edit import FormView

from django.contrib.auth import authenticate, logout as LOGOUT, login as LOGIN
from django.contrib.auth.models import User

from . import forms

# Create your views here.

def logout(request):
    if request.user.is_authenticated:
        LOGOUT(request)
        return HttpResponseRedirect('/home/')

class UserAuthorizationView(FormView):
    form_class = forms.UserAuthorizationForm

    success_url = '/home/'

    template_name = 'accounts/authorization.html'
    

    def form_valid(self,form):
        cleaned_data = form.clean()
        login = cleaned_data['login']
        password = cleaned_data['password']

        user = authenticate(self.request, username=login, password=password)

        if user is not None :
            LOGIN(self.request, user)
        else:
            form.add_error('password', "Wrong login or password!")
            return self.form_invalid(form)

        return super(UserAuthorizationView,self).form_valid(form)
    
    def form_invalid(self,form):
        return super(UserAuthorizationView,self).form_invalid(form)

class UserRegistrtionView(FormView):
    form_class = forms.UserRegistrtionForm

    success_url = '/home/'

    template_name = 'accounts/registration.html'

    def form_valid(self,form):

        cleaned_data = form.clean()
        
        if  len(cleaned_data)>0:
            self.save_user(cleaned_data)
        else:
            return self.form_invalid(form)

        
        return super(UserRegistrtionView,self).form_valid(form)

    def save_user(self,cleaned_data):
        User.objects.create_user(username=cleaned_data['login'],
                                 email=cleaned_data['email'],
                                 password=cleaned_data['password_first']
                                )


    def form_invalid(self,form):
        return super(UserRegistrtionView,self).form_invalid(form)