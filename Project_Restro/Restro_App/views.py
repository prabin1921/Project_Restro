from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'GET':
        content = {
            'msg': 'Hello!',
            'page_title': 'Home'
        }
        return render(request, "App\home.html", content)
    



# def home(request):
#     # View code here...
#     return render(
#         request,
#         "C:\Users\User\Desktop\Projects\Project_Restro\Templates\Restro_App\home.html",
#     )