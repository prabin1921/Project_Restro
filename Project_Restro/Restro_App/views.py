from datetime import datetime 
from django.shortcuts import (render,redirect, HttpResponse,
                              get_object_or_404, get_list_or_404)
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
    # booking=Reservation.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        number=request.POST.get("number")
        date_and_time = datetime.strptime(request.POST.get("datetime"),'%Y-%m-%dT%H:%M')
        people=request.POST.get("people")
        table_id=request.POST.get("table_id")
        special_request=request.POST.get("special_request")
        table = get_object_or_404(Table, pk=table_id)
        print(table.price)
        
        
        if Reservation.objects.filter(table = table).exists():
            messages.error(request, 'This table is already Booked! Please select next one')
            return redirect('booking')
        
        else:
            # table = Reservation.objects.get(table)
            data, created = Reservation.objects.get_or_create(name =name,email=email, number= number, datetime=date_and_time, people=people, table=table, special_request=special_request )
            # messages.alert(request, 'The price for this table is'+ (price) + 'are you sure to book?')
        
        return render(request, 'pages/booking.html', {'data':data})
    
    tables = get_list_or_404(Table)
    context = {
        'tables': tables
    }
    return render(request, 'pages/booking.html',context)


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