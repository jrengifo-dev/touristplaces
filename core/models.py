from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    names = models.CharField(max_length=150)
    last_names = models.CharField(max_length=150)
    document_number = models.CharField(max_length=20, unique=True)
    cellphone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='persons/', null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.document_number})-{self.names} {self.last_names}"
    
class Ubigeo(models.Model):
    code = models.CharField(max_length=6, unique=True)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.code} - {self.region} - {self.province} - {self.district}"
    

class Place(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    description = models.TextField()
    content=models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    ubigeo = models.ForeignKey(Ubigeo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.address}"
    
class Gallery(models.Model):
    file = models.ImageField(upload_to='places/gallery/')
    index = models.IntegerField(null=True, blank=True)
    is_frontpage = models.BooleanField(default=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}-{self.place.name}"
    
class Review(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.person.names} for {self.place.name}"