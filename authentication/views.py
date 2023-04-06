from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from authentication.models import User, Warn
from .forms import SignUpForm, LoginForm


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
        return render(request, 'authentication/login.html', {'form': form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Erfolgreich angemeldet!')
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


class UserUpdateView(generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email', 'birthdate']
    template_name = "authentication/user_update.html"

    def get_success_url(self):
        return reverse_lazy('user', args=[self.object.pk])

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context


def user_delete(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('feeds')
    return (request, 'authentication/user_delete.html', {'user': user})


class WarnCreateView(generic.CreateView):
    model = Warn
    fields = ['reason']
    template_name = "authentication/warn_create.html"

    def get_success_url(self):
        return reverse_lazy('user_warns', kwargs={"pk": self.kwargs.get('user_id')})

    def get_current_user(self, **kwargs):
        return User.objects.get(id=self.kwargs.get('user_id'))

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.get_current_user(**kwargs)
        data.update({'user': user})
        return data

    def form_valid(self, form):
        form.instance.user = self.get_current_user(**self.kwargs)
        return super().form_valid(form)


def warn_delete(request, pk):
    warn = get_object_or_404(Warn, pk=pk)

    if request.method == 'POST':
        user_id = warn.user.id
        warn.delete()
        return redirect('user_warns', pk=user_id)
    return JsonResponse({'success': False})
