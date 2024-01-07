from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100)
    content =models.CharField(max_length=200)
    film = models.FileField(upload_to='Film', default='film')

    def __str__(self):
        return self.title


class Menu(models.Model):
    image = models.ImageField(upload_to='Menu',default='Menu.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title





class MenuSpecials(models.Model):
    image = models.ImageField(upload_to='MenuSpecials',default='MenuSpecials.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    content2 = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    




class EventsRestaurant(models.Model):
    image = models.ImageField(upload_to='Event',default='Event.jpg')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title





class Order(models.Model):
    pass




class Comment(models.Model):
    pass



class PhotosRestaurant:
    pass



class Chefs(models.Model):
    pass


class ContactUs(models.Model):
    pass






