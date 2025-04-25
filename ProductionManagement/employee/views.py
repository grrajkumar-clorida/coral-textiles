from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
#from .models import Employees
from production.models import Production
from production.forms import ProductionForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.
def home(request):
    user = authenticate(username='bhuvi', password='demo@123')
    if user is not None:
        print("User authenticated successfully")
    else:
        print("Invalid username or password")
    #employees = User.objects.all()
    return render(request, 'home.html')

def about_us(request):
	return render(request, 'about_us.html')

@login_required
def log_report(request):
    #return render(request, 'home.html')
    if request.method == 'POST':
        form = ProductionForm(request.POST, request.FILES)
        if form.is_valid():
            production = form.save(commit=False)
            production.user = request.user  # Attach the logged-in user
            production.save()
            messages.success(request, 'Production record has been added successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductionForm()
    return render(request, 'log_report.html', {'form': form})

@login_required
def production_report(request):
	# Retrieve all the Production records created by the logged-in user
	productions = Production.objects.filter(employee=request.user)
	return render(request, 'production_report.html', {'productions':productions})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


