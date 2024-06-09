from django.contrib import admin
from .models import HouseListing, ImageModel

# Register your models here.
class ImageModelInline(admin.TabularInline):
    model = ImageModel
    extra = 1
    
    
class HouseListingAdmin(admin.ModelAdmin):
    list_display = ('house_name', 'total_contract_price', 'property_type', 'address', 'city', 'lot_area', 'location_coordinates', 'contact_agent')
    search_fields = ['house_name', 'contact_agent', 'property_type']
    list_filter = ['city', 'property_type']
    inlines = [ImageModelInline]
    
admin.site.register(HouseListing, HouseListingAdmin)