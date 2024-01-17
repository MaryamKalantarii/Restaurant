from django.shortcuts import render,redirect
from .models import Service,Category,Menu,MenuSpecials,Order,EventsRestaurant,Skills,Chefs,RestaurantInformation
from django.contrib import messages
from .forms import OrderForm,ContactUsForm

def home(request):
    if request.method == 'GET':
        servic = Service.objects.filter(status = True)
        menu = Menu.objects.filter(status = True)
        menuspecial = MenuSpecials.objects.filter(status = True)
        eventsrestaurant = EventsRestaurant.objects.filter(status = True)
        chef = Chefs.objects.filter(status = True)
        skills = Skills.objects.all()
        context = {
            'servic':servic,
            'menu':menu,
            'menuspecial':menuspecial,
            'eventsrest': eventsrestaurant,
            'chef':chef,
            'sk':skills,
            
            }
        return render(request,"root/index.html",context=context)
    
    elif request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you you as soon')
            return redirect('root:home')
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:home')

    
    
        

    

