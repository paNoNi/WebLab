from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from Auth.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

from Auth.models import Profile


def index(request):
    return redirect(reverse(register))


def register(request):
    print(request)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с этим электронным адресом уже зарегестрирован')
        else:
            if form.is_valid():
                ins = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password, email=email)
                login(request, user)
                ins.email = email
                ins.save()
                form.save_m2m()
                messages.success(request, 'Вы успешно зарегестрировались!')
                return redirect('tasks')

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'auth/register.html', context)


class ProfileDetail(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'sod/profile.html'
