from django.shortcuts import render,redirect
from .models import*


# Home View
def home(request):
    return render(request, "home.html")
    
    
# About view
def aboutUs(request):
    return render(request, "pages/about.html")


# Boooking 'View    
def booking(request):
    booking=BookTable.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        number=request.POST.get("Number")
        datetime=request.POST.get("datetime")
        people=request.POST.get("person")
        specialRequest=request.POST.get("message")
        
        data = BookTable.objects.create(Name=name, Email=email, Ph_Number=number, DateTime=datetime, No_People=people, SpecialRequest=specialRequest)
        # redirect('booking')
    
    return render(request, 'pages/booking.html')

# conatct View
def contact(request):
    return render(request, 'pages/contact.html')

# Menu View
def Menu(request):
    return render(request, 'pages/menu.html')

# Service View
def Service(request):
    return render(request, 'pages/service.html')


    



# def home(request):
#     # View code here...
#     return render(
#         request,
#         "C:\Users\User\Desktop\Projects\Project_Restro\Templates\Restro_App\home.html",
#     )