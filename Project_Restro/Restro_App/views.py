from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"app/home.html", {})

# def home(request):
#     # View code here...
#     return render(
#         request,
#         "C:\Users\User\Desktop\Projects\Project_Restro\Templates\Restro_App\home.html",
#     )