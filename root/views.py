from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Service,Category,Menu,MenuSpecials,Order,EventsRestaurant,PhotosRestaurant,Skills,Chefs,ContactUs,RestaurantInformation
from django.contrib import messages
from .forms import OrderForm

def home(request):
    if request.method == 'GET':
        servic = Service.objects.filter(status = True)
        menu = Menu.objects.filter(status = True)
        menuspecial = MenuSpecials.objects.filter(status = True)
        eventsrestaurant = EventsRestaurant.objects.filter(status = True)

        context = {
            'servic':servic,
            'menu':menu,
            'menuspecial':menuspecial,
            'eventsrest': eventsrestaurant
            
            }
        return render(request,"root/index.html",context=context)
    
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you you as soon')
            return redirect('root:contact')
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')

    
    
        

    

