from django.db.models import Q
from django.shortcuts import render
from.models import HouseListing

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listings(request):
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    min_lot_area = request.GET.get('min_lot_area', '')
    max_lot_area = request.GET.get('max_lot_area', '')
    city = request.GET.get('city', '')
    property_type = request.GET.get('property_type', '')
    
    q_objects = Q()
    
    if min_price:
        q_objects.add(Q(total_contract_price__gte=min_price), Q.AND)
    if max_price:
        q_objects.add(Q(total_contract_price__lte=max_price), Q.AND)
    if min_lot_area:
        q_objects.add(Q(lot_area__gte=min_lot_area), Q.AND)
    if max_lot_area:
        q_objects.add(Q(lot_area__lte=max_lot_area), Q.AND)
    if city:
        q_objects.add(Q(city__icontains=city), Q.AND)
    if property_type:
        q_objects.add(Q(property_type__icontains=property_type), Q.AND)
    
    if min_price or max_price or min_lot_area or max_lot_area or city or property_type:
        house_listings = HouseListing.objects.filter(q_objects).distinct()
    else:
        house_listings = HouseListing.objects.all()
    
    return render(request, 'listings.html', {'house_listings': house_listings})