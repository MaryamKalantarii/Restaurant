from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Service,Category,Menu,MenuSpecials,Order,EventsRestaurant,PhotosRestaurant,Skills,Chefs,ContactUs,RestaurantInformation


class HomeView(TemplateView):
    Model = Service
    template_name = 'root/index.html'
    




