from django.shortcuts import render, redirect
from .models import Branch,CountryOfOrigin,Category,Product,Sale
from .forms import BranchCreationForm,CountryOfOriginCreationForm,CategoryCreationForm,ProductCreationForm,SaleCreationForm, UserRegistrationForm
#importing login,logout,
from django.contrib.auth import authenticate, login,logout
#importing messages
from django.contrib import messages

from django.contrib.auth.decorators import login_required






# Create your views here.

@login_required
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'spare/home.html', context)


def create_branch(request):
    if request.method == 'POST':
       form = BranchCreationForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('home') 

    form = BranchCreationForm()
    context = {'form':form}
    return render(request, 'spare/form.html',context)



def create_country(request):
    if request.method == 'POST':
       form = CountryOfOriginCreationForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('home') 

    form = CountryOfOriginCreationForm()
    context = {'form':form}
    return render(request, 'spare/form.html',context)


def create_category(request):
    if request.method == 'POST':
       form = CategoryCreationForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('home') 

    form = CategoryCreationForm()
    context = {'form':form}
    return render(request, 'spare/form.html',context)


def create_product(request):
    if request.method == 'POST':
       form = ProductCreationForm(request.POST) 
       
       if form.is_valid():
            form.save()

            return redirect('home') 

    form = ProductCreationForm()
    context = {'form':form}
    return render(request, 'spare/form.html',context)

def create_sale(request):
    if request.method == 'POST':
       form = SaleCreationForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('home') 

    form = SaleCreationForm()
    context = {'form':form}
    return render(request, 'spare/form.html',context)


def register(request):
    if request.method == 'POST':
       form = UserRegistrationForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('home') 

    form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'spare/form.html',context)



def SignUp(request):
    return render(request,'spare/signup.html')


def base(request):
    return render(request,'spare/base.html')






