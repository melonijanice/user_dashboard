from django.shortcuts import redirect, render

# Create your views here.
def welcome(request):
    request.session.flush()
    return render(request,'welcome.html')

def dashboard(request):
    if request.method=="GET":
        return redirect('/')
    if request.method=="POST":
        return render(request,'user_dashboard.html')

