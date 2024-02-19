from django.shortcuts import render


# Home View
def home(request):
    return render(request, "home.html")
    
    
# About view
def aboutUs(request):
    return render(request, "pages/about.html")


# Boooking 'View    
def booking(request):
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