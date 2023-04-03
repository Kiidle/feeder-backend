from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from authentication.models import User

def logout_view(request):
    logout(request)
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "authentication/signup.html"

@login_required
def custom_logout(request):
    logout(request)
    return redirect("login")

def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        form = LoginForm()
        return render(request,'authentication/login.html', {'form': form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Erfolgreich angemeldet!')
                return redirect('feeds')

        messages.error(request, f'Benutzername oder Passwort ist falsch.')
        return render(request, 'authentication/login.html', {'form': form})

class UsersView(generic.ListView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'birthdate', 'verified']
    template_name = 'authentication/users.html'

class UserView(generic.DetailView):
    model = User
    template_name = 'authentication/user.html'

class UserCommentariesView(generic.DetailView):
    model = User
    template_name = 'authentication/user_commentaries.html'

class UserWarnsView(generic.DetailView):
    model = User
    template_name = 'authentication/user_warns.html'

def redirectURL(request):
    return redirect('feeds')