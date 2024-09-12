from django.shortcuts import render,redirect
from django.http import HttpResponse
from ecommerce.forms import signup
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from ecommerce.models import catagory,products,cart
from django.contrib.auth.models import User
# Create your views here.

# sign up
def signup1(request):
    if request.method =="POST":
        fm=signup(request.POST)
        if fm.is_valid():
            messages.info(request,"user creation successfully")
            fm.save()
    else:
        fm=signup()
    return render(request,'signup.html',{'form':fm})
 
# login
def login1(request):
    if request.method=="POST":
        fm=AuthenticationForm(request,data=request.POST)
        if fm.is_valid():
            name1=fm.cleaned_data['username']
            password1=fm.cleaned_data['password']
            allow=authenticate(request,username=name1,password=password1)
            if allow is not None:
                login(request,allow)
                return redirect('main')
            else:
                return redirect('login')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'fm':fm})

def main(request):
    catagory2=catagory.objects.filter(status=0)
    return render(request,'main.html',{'items':catagory2})

# log out
def logout1(request):
    logout(request)
    return redirect('main')

# category page
def catagory1(request):
    catagory2=catagory.objects.filter(status=0)
    print('hii',catagory2)
    return render(request,'catagory.html',{'items':catagory2})

# collections
def collections(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        collect=products.objects.filter(catagory__name=name)
        print(collect)
    return render(request,'collection.html',context={'collection':collect,'gat':name})

# product page
def product(request,name):
    if(products.objects.filter(name=name,status=0)):
        product=products.objects.filter(name=name).first()
        print('name',product.name,'description',product.description,'image_url',product.image.url)
    return render(request,'product.html',{'product':product})


def add_cart(request,use,pro):
    pass


