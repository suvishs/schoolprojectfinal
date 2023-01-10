from . models import department, employee
# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def home(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'new.html')
        else:
            messages.info(request,'invalid')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirm_password')
    #
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();

                return redirect(login)
        else:
            messages.info(request, "Password not matching")
            return redirect('register')

    return render(request,'register.html')


def application_form(request):
    if request.method == 'POST':
        messages.success(request, "Order Confirmed")
        return redirect('last_page')
    deptcontext = department.objects.all()
    empcontext = employee.objects.all()
    return render(request, 'application_form.html', {'department': deptcontext, 'employee': empcontext})

def last_page(request):
    return render(request,'last_page.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
