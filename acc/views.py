from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from datetime import timedelta as td
from django.http import JsonResponse

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
        duration_logged_in = round_nearest_minute(duration_logged_in)
    else:
        duration_logged_in = None
    return render(request, 'account.html', {'user': user, 'duration_logged_in': duration_logged_in})

def round_nearest_minute(td):
    """
    Rounds off a timedelta object to the nearest minute.

    Args:
        td (timedelta): The timedelta object to round off.

    Returns:
        int: The rounded off value in minutes.
    """
    total_seconds = td.total_seconds()
    minutes = total_seconds // 60
    remainder = total_seconds % 60
    if remainder >= 30:
        minutes += 1
    return int(minutes)

def dynamic_content_view(request):
    # Logic to retrieve updated dynamic content
    # For demonstration purposes, let's assume we have a function to calculate the duration logged in
    duration_logged_in = account_view(duration_logged_in)
    
    # Render the updated dynamic content as HTML
    updated_content_html = f'<h2>Welcome, {request.user.username}</h2>'
    updated_content_html += f'<p>You have been active for: <span id="duration_logged_in">{duration_logged_in}</span> Minutes</p>'
    
    # Return the updated content as JSON response
    return JsonResponse({'updated_content': updated_content_html})

