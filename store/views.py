from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# for user register 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm
from django import forms

# Create your views here.
def home(request):
    products=Product.objects.all()
    category=Category.objects.all()

    return render(request,'store/home.html',{'products':products,'category':category})


def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')


# single product view
def product_view(request,pk):
      product=Product.objects.get(id=pk)
      return render(request,'store/product_view.html',{'product':product})





def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
        
            login(request,user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('home')
        else:
            messages.success(request,("Invalid Credentials "))
            return redirect('login')
		   
    
    return render(request,'store/login.html')

    

def register(request):
   
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
        
        
		if form.is_valid():
   
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You Have Registered Successfully!! Welcome!"))
			return redirect('home')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'store/register.html', {'form':form})
    


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out...Thanks for stopping by..."))
    return redirect('home')
    # return render(request,'store/logout.html')


def about(request):
    return render(request,'store/about.html')


def category(request):
    category=Category.objects.all()
    return render(request,'store/category.html',{'category':category})