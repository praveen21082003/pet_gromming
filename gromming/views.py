from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import JsonResponse
from .forms import CustomizePackageForm
from .models import CustomizePackage  # just in case it's not imported
# Create your views here.

def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')  # Using `.get()` to avoid errors
        first_name = request.POST.get('first_name', '')  # Changed to `first_name`
        last_name = request.POST.get('last_name', '')  # Changed to `last_name`
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect('home')

    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('pwd')  # Ensure the input name matches your form

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')

    return render(request, 'login.html')  # Ensure it returns the login page for GET requests



def logout_user(request):
    logout(request)
    return redirect('home')




def get_user(request):
    if request.user.is_authenticated:
        return JsonResponse({"is_authenticated": True, "username": request.user.username})
    else:
        return JsonResponse({"is_authenticated": False})
    





def service(request):
    if request.method == 'POST':
        form = CustomizePackageForm(request.POST, request.FILES) # Added request.FILES to handle file uploads
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # 🔗 connect booking to logged-in user
            booking.save()
            form.save_m2m()  # for services ManyToMany field
            return redirect('services') 
    else:
        form = CustomizePackageForm()
    
    return render(request, 'service.html', {'form': form})


