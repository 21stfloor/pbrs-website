from django.contrib import admin
from .models import HouseListing

# Register your models here.
class HouseListingAdmin(admin.ModelAdmin):
    list_display = ('house_name', 'total_contract_price', 'type_of_house', 'address', 'location_coordinates', 'contact_agent')
    search_fields = ('house_name', 'type_of_house', 'address', 'contact_agent')
    list_filter = ('type_of_house', 'contact_agent')
    
admin.site.register(HouseListing, HouseListingAdmin)