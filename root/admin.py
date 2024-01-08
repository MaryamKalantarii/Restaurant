from django.contrib import admin
from .models import Service,Category,Menu,MenuSpecials,Order,EventsRestaurant,PhotosRestaurant,Skills,Chefs,ContactUs,RestaurantInformation
# Register your models here.

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(MenuSpecials)
admin.site.register(Order)
admin.site.register(EventsRestaurant)
admin.site.register(PhotosRestaurant)
admin.site.register(Skills)
admin.site.register(Chefs)
admin.site.register(ContactUs)
admin.site.register(RestaurantInformation)
