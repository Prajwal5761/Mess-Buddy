from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from app1.models import Profile
from django.db.models import Sum

# Create your views here.

@login_required
def DashPage(request):
    return render (request, 'dashboard.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username1')
        email = request.POST.get('email1')
        pass1 = request.POST.get('password1')
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        # Create a new Profile object for the user
        Profile.objects.create(user=my_user)
        return redirect('dashboard')
    
    return render(request, 'index.html')

def Signup_LoginPage(request):
    if request.method == 'POST':
        # Check if the user is trying to login
        if 'login' in request.POST:
            # Handle login logic here
            # Redirect to dashboard or display error messages    
            username = request.POST.get('username')
            pass1 = request.POST.get('password') 
            user = authenticate(request, username=username, password=pass1)
            if user is not None:
                # Get the Profile object for the user
                login(request, user)
                profile = Profile.objects.get_or_create(user=user)
                return redirect('dashboard')
            else:
                return HttpResponse("Username or Password is incorrect!!!")
            
        elif 'register' in request.POST:
            # Handle registration logic here
            # Redirect to dashboard or display error messages
            uname = request.POST.get('username1')
            email = request.POST.get('email1')
            pass1 = request.POST.get('password1')
            my_user = User.objects.create_user(email=email, username=uname, password=pass1)
            my_user.save()   
            return redirect('signup')
    
    return render(request, 'index.html')

def LoginPage(request):
    return render (request, 'index.html') 

def LogoutPage(request):
    logout(request)
    return redirect('signup')

def AboutPage(request):
    return render(request, 'about.html')

def ContactPage(request):
    return render(request, 'contact.html')

def MenuPage(request):
    return render(request, 'home.html')

def LunchPage(request):
    # If the user has already selected an item for the day, retrieve it from the session
    if 'selected_item' in request.session:
        selected_item = request.session['selected_item']
    else:
        selected_item = None

    return render(request, 'lunch.html', {'selected_item': selected_item})

@login_required
def GetData(request):
    user = request.user
    profile = user.profile
    context = {
        'username': user.username,
        'email': user.email,
        'breakfast_amt': profile.breakfast_amt,
        'plates': profile.plates,
    }
    return render(request, 'data.html', context)

@login_required
def TotalAmt(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('item')  # Get the list of selected items
        total_amount = 0
        

        # Calculate total amount
        for item_name in selected_items:
            item_price = int(request.POST.get(f"{item_name}_price", 0))  # Retrieve the price of the item
            total_amount += item_price
        
        # Add total amount to user's profile
        if request.user.is_authenticated:
            profile = request.user.profile
            profile.breakfast_amt += total_amount
            profile.save()

        return render(request, 'total_amount.html', {'total_amount': total_amount, 'selected_items': selected_items})
    else:
        return HttpResponse("Method not allowed")
    
@login_required
def TotalPlates(request):
    if request.method == 'POST':
        plates_no = 1  # Set plates_no to 1, as the user is selecting only one option at a time

        if request.user.is_authenticated:
            profile = request.user.profile
            profile.plates += plates_no
            profile.save()

        # Save the selected item in the user's session so that it remains selected for the day
        selected_item = request.POST.getlist('item')
        
        request.session['selected_item'] = selected_item

        return render(request, 'lunch.html', {'selected_item': selected_item})
    else:
        # If the user has already selected an item for the day, retrieve it from the session
        if 'selected_item' in request.session:
            selected_item = request.session['selected_item']
        else:
            selected_item = None

        return render(request, 'lunch.html', {'selected_item': selected_item})
    
def profile_listPage(request):
    profiles = Profile.objects.all()
    total_breakfast_amt = sum(profile.breakfast_amt for profile in profiles)
    total_plates = sum(profile.plates for profile in profiles)
    context = {
        'profiles': profiles,
        'total_breakfast_amt': total_breakfast_amt,
        'total_plates': total_plates,
    }
    return render(request, 'profile_list.html', context)

def BillPage(request):
    return render(request, 'page1.html')

def TotalBillPage(request):
    rate_per_plate = request.POST.get('rate_per_plate')
    service_charges = request.POST.get('service_charges')

    profiles = Profile.objects.all()

    total_breakfast_amount = profiles.aggregate(Sum('breakfast_amt'))['breakfast_amt__sum'] or 0
    total_plates = profiles.aggregate(Sum('plates'))['plates__sum'] or 0
    total_final_amount = total_breakfast_amount + total_plates * int(rate_per_plate) + int(service_charges) * profiles.count()

    for profile in profiles:
        profile.lunch_amt = profile.plates*int(rate_per_plate)

    context = {
        'profiles': profiles,
        'rate_per_plate': rate_per_plate,
        'service_charges': service_charges,
        'total_final_amount': total_final_amount,
    }

    return render(request, 'page2.html', context)