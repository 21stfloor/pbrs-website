from django.db import models

# Create your models here.
class HouseListing(models.Model):
    house_name = models.CharField(max_length=100)
    total_contract_price = models.DecimalField(max_digits=10, decimal_places=2)
    type_of_house = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location_coordinates = models.CharField(max_length=100)
    contact_agent = models.CharField(max_length=100)
    
    def __str__(self):
        return self.house_name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='house_images/')
    house_listing = models.ForeignKey(HouseListing, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.house_listing.house_name