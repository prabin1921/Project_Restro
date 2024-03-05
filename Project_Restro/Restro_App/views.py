from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from .models import*
from .forms import*





# Home View
def home(request):
    return render(request, "home.html")
    
    
# About view
def aboutUs(request):
    return render(request, "pages/about.html")


# Boooking 'View    
def booking(request):
    # booking=BookTable.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        number=request.POST.get("number")
        datetime=request.POST.get("datetime")
        people=request.POST.get("no_people")
        table_no=request.POST.get("table_no")
        special_request=request.POST.get("special_request")
        
        if BookTable.objects.filter(table_no = table_no).exists():
            messages.error(request, 'This table is already Booked! Please select next one')
            return redirect('booking')
        
        data = BookTable.objects.create(name=name, email=email, number=number, datetime=datetime, no_people=people, special_request=special_request, table_no=table_no)
        
        return render(request, 'pages/booking.html', {'data':data})
    
    return render(request, 'pages/booking.html')


# conatct View
def contact(request): 
    return render(request, 'pages/contact.html')

# Menu View
def Menu(request):
    # if request.method == 'GET':
    #     print(request)
    categories = Category.objects.all()
    foodmenu = FoodMenu.objects.all()
    if request.method == 'POST':
        form = FoodMenuItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu') 
    else:
        form = FoodMenuItemsForm()

    context = {
        'foodmenu': foodmenu,
        'categories': categories,
        'form': form,
    }
        
    return render(request, 'pages/menu.html', context)

def Add_Items(request, id):
    item =  get_object_or_404(FoodMenu, pk=id)
    if request.method == 'POST':
        form = FoodMenu(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = FoodMenu(instance=item)
    
    
    return render(request, 'pages/menu.html', {'form':form})

# Service View
def Service(request):
    return render(request, 'pages/service.html')


    



# def home(request):
#     # View code here...
#     return render(
#         request,
#         "C:\Users\User\Desktop\Projects\Project_Restro\Templates\Restro_App\home.html",
#     )