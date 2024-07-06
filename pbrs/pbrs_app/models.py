from django.db import models
from django.utils.timezone import now

# Create your models here.
class HouseListing(models.Model):
    house_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    total_contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    lot_area = models.DecimalField(max_digits=10, decimal_places=2)
    location_coordinates = models.CharField(max_length=100, blank=True, default='')
    contact_agent = models.CharField(max_length=100)
    financing = models.CharField(max_length=64, default='', blank=True)
    agent_phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.house_name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='house_images/')
    house_listing = models.ForeignKey(HouseListing, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.house_listing.house_name