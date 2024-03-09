from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account')  # Redirect to account home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def account_view(request):
    user = request.user
    if user.is_authenticated:
        duration_logged_in = timezone.now() - user.last_login
    else:
        duration_logged_in = None
    return render(request, 'account.html', {'user': user, 'duration_logged_in': duration_logged_in})



