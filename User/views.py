from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import userRegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'{username} your account has been created, Please Login!')
            return redirect('login')
    else:
        form = userRegisterForm()
    return render(request, 'User/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'User/profile.html')