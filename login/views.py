from django.http.response import HttpResponse, JsonResponse
from login.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
import bcrypt

# Create your views here.

def sign_in(request):
    return render(request,'login.html')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/signin')
    else:
        logged_user = User.objects.get(email=request.POST['email'])
        request.session['user_id']=logged_user.id
        return redirect('/dashboard')


def register(request):
    if request.method== "GET":
        return render(request,'registration.html')
    if request.method== "POST":
        errors = User.objects.registration_validator(request.POST)
            # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key,value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/register')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
            user_id=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash)
            request.session['user_id']=user_id.id
            return redirect('/dashboard')
    
def validate(request):
    email = request.POST['email']
    data = {
        'taken' : User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)