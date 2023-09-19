from django.shortcuts import render, redirect
from emp_register.models import EmpRegister
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm, AddEmployeeForm, UpdateEmployeeForm
from django.db.models import Q

# Create your views here.

def home(request):
    emp = EmpRegister.objects.all()
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password'] 

        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Logged In!")
            return redirect('home')
            
        else:
            messages.success(request, 'There Was An Error Logging In, Try Agian!')
            return redirect('home')
    else:
        if 'srch' in request.GET:
            srch =request.GET['srch']
            mult_srch = Q(Q(name__icontains= srch) | Q(designation__icontains=srch))
            emp = EmpRegister.objects.filter(mult_srch)

        return render(request, 'home.html', {"emp":emp})
        

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out!')
    return render(request, 'home.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username = username, password=password)
            login(request, user)
            messages.success(request, 'Welcome! You Have Been Registered')
            return redirect('home')
    else:
        form  = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})
    
def del_emp(request,id):
    if request.user.is_authenticated:
        emp = EmpRegister.objects.get(id=id)
        emp.delete()
        messages.success(request, 'Employee has been delted!')
        return redirect('home') 
    else:
        messages.success(request, 'Please Login to continue!')
        return redirect('home')
        
def add_emp(request):

    empForm = AddEmployeeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if empForm.is_valid():
                add_record = empForm.save()
                messages.success(request, 'Employee Added!')
                return redirect('home')
        return render(request, 'add_emp.html', { 'form': empForm } )
    else:
        messages.success(request, 'Please Login!')
        return redirect('home')


def update_emp(request, id):
    if request.user.is_authenticated:
        emp = EmpRegister.objects.get(id=id)
        
        empForm = UpdateEmployeeForm(request.POST or None, instance=emp)
        if empForm.is_valid():
            empForm.save()
            messages.success(request, 'Employee Details Updated!')
            return redirect('home')
        return render(request, 'update_emp.html', { 'form': empForm })
    else:
        messages.success(request, 'Please Login!')
        return redirect('home')


