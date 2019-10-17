from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def Login_Reg(request):
    return render(request, 'login_reg_app/login_reg.html')

def Register(request):
    print(request.POST)
    errors = User.objects.validate_register(request.POST)
    if len(errors) > 0:
        print("Errors",errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash.decode())
        print("User: ", user)
        request.session['id'] = user.id
    return redirect('/wall')

def Login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['id'] = user.id
    return redirect('/wall')

def Success(request):
    user = User.objects.get(id=request.session['id'])
    return render(request, 'login_reg_app/success.html', {'user':user})

def Logout(request):
    request.session.clear()
    print("Logged Out")
    return redirect('/')


