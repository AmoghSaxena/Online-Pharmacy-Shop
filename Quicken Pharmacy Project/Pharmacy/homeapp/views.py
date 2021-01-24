from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductDetails, Newsletter, ContactUs, Login, Registeration


#Method to create home page
def index(request):
    return render(request,"homeapp/index.html")

#Method to create login page
def login(request):
    return render(request,"homeapp/login.html")

#Method to create registeration page
def register(request):
    return render(request,"homeapp/registration.html")

#Method to create blog page
def blog(request):
    return render(request,"homeapp/blog.html")

#Method to create cart page
def cart(request):
    return render(request,"homeapp/cart.html")

#Method to create category page
def category(request):
    return render(request,"homeapp/category.html")

#Method to create checkout page
def checkout(request):
    return render(request,"homeapp/checkout.html")

#Method to create confirmation page
def confirmation(request):
    return render(request,"homeapp/confirmation.html")

#Method to create contact page
def contact(request):
    return render(request,"homeapp/contact.html")

#Method to create elements page
def elements(request):
    return render(request,"homeapp/elements.html")

#Method to create single-blog page
def singleblog(request):
    return render(request,"homeapp/singleblog.html")

#Method to create single-blog page
def singleblog2(request):
    return render(request,"homeapp/singleblog2.html")

#Method to create single-blog page
def singleblog3(request):
    return render(request,"homeapp/singleblog3.html")

#Method to create single-blog page
def singleblog4(request):
    return render(request,"homeapp/singleblog4.html")

#Method to create single-blog page
def singleblog5(request):
    return render(request,"homeapp/singleblog5.html")

#Method to create single-product page
def singleproduct(request):
    return render(request,"homeapp/single-product.html")

#Method to create tracking page
def tracking(request):
    return render(request,"homeapp/tracking.html")

#Method to create Terms And Condition
def tandc(request):
    return render(request,"homeapp/termsandconditions.html")


#To Check The validate username
def checkrno(request):
    n = request.GET.get("q")
    s = Registeration.objects.filter(username=n)
    if len(s)>0:
       return HttpResponse("Username is already taken Please choose new Username")
    else:
       return HttpResponse("Valid")

#Method to take input from User in registration page
def inputreg(request):
    Name = request.POST["name"]
    UserName = request.POST["username"]
    Password = request.POST["password"]
    Email = request.POST["email"]
    DataStore = Registeration(email=Email, name=Name, username=UserName, password=Password)
    DataStore.save()
    return render(request, "homeapp/registration.html",{'key':'Data Inserted Sucessfully, Please Login now'})


#To take email form newsletter form
def newsletter(request):
    Email = request.GET["EMAIL"]
    data = Newsletter(email=Email)
    data.save()
    return render(request, "homeapp/registration.html")