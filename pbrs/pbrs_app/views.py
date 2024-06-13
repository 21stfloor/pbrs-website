from django.db.models import Q
from django.shortcuts import render
from.models import HouseListing

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listings(request):
    query = request.GET.get('query', '')
    if query:
        house_listings = HouseListing.objects.filter(
            Q(house_name__icontains=query) | Q(contact_agent__icontains=query) | Q(type_of_house__icontains=query)
        )
    else:
        house_listings = HouseListing.objects.all()
    return render(request, 'listings.html', {'house_listings': house_listings})

def about(request):
    return render(request, 'about.html')