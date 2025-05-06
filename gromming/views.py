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


from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        name = request.POST.get('name', '') 
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')  # or render the same page with error

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return redirect('register')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = name 
            user.save()
            return redirect('home')
        else:
            messages.error(request, "Password does not match!")

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


def customize_package_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        address = request.POST.get('address')

        pet_name = request.POST.get('petname')
        pet_type = request.POST.get('pettype')
        pet_breed = request.POST.get('petbreed')
        pet_age = request.POST.get('petage')
        pet_gender = request.POST.get('petgender')
        pet_weight = request.POST.get('petweight')
        pet_height = request.POST.get('petheight')
        pet_medical_condition = request.POST.get('petmedicalcondition')
        pet_vaccination_status = request.POST.get('petvaccination')

        pet_image = request.FILES.get('petimage')

        booking_date = request.POST.get('appointmentdate')
        booking_time = request.POST.get('appointmenttime')
        package_type = request.POST.get('petservices')

        customize_package = CustomizePackage(
            user=request.user,
            fullname=fullname,
            phonenumber=phonenumber,
            email=email,
            address=address,
            pet_name=pet_name,
            pet_type=pet_type,
            pet_breed=pet_breed,
            pet_age=pet_age,
            pet_gender=pet_gender,
            pet_weight=pet_weight,
            pet_height=pet_height,
            pet_medical_condition=pet_medical_condition,
            pet_vaccination_status=pet_vaccination_status,
            pet_image=pet_image,
            booking_date=booking_date,
            booking_time=booking_time,
            package_type=package_type,
            status='will update soon'
        )
        customize_package.save()

        return redirect('my_bookings')  # ✅ Give your correct success page here

    return render(request, 'service.html')  # ✅ Your actual form template here



# This block of code is redundant and should be removed as it is outside any function.
# If needed, ensure similar logic is already implemented within a valid function.



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Booking

from .models import CustomizePackage  # ensure this is imported

@login_required
def my_bookings(request):
    bookings = CustomizePackage.objects.filter(user=request.user)
    return render(request, 'mybooking.html', {'bookings': bookings})






