from django.db.models import Q, Min, Max
from django.shortcuts import render
from.models import HouseListing

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listings(request):
    query = request.GET.get('query', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    min_lot_area = request.GET.get('min_lot_area', '')
    max_lot_area = request.GET.get('max_lot_area', '')
    city = request.GET.get('city', '')
    property_type = request.GET.get('property_type', '')
    
    q_objects = Q(house_name__icontains=query) | Q(contact_agent__icontains=query) | Q(property_type__icontains=query)
    
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
    
    if query or min_price or max_price or min_lot_area or max_lot_area or city or property_type:
        house_listings = HouseListing.objects.filter(q_objects).distinct()
    else:
        house_listings = HouseListing.objects.all()
    
    min_price_value = HouseListing.objects.aggregate(Min('total_contract_price'))['total_contract_price__min']
    max_price_value = HouseListing.objects.aggregate(Max('total_contract_price'))['total_contract_price__max']
    min_lot_area_value = HouseListing.objects.aggregate(Min('lot_area'))['lot_area__min']
    max_lot_area_value = HouseListing.objects.aggregate(Max('lot_area'))['lot_area__max']
    cities = HouseListing.objects.values_list('city', flat=True).distinct()
    property_types = HouseListing.objects.values_list('property_type', flat=True).distinct()
    
    return render(request, 'listings.html', {
        'house_listings': house_listings,
        'min_price': min_price_value,
        'max_price': max_price_value,
        'min_lot_area': min_lot_area_value,
        'max_lot_area': max_lot_area_value,
        'cities': cities,
        'property_types': property_types,
        'selected_city': city,
        'selected_type': property_type,
    })

def about(request):
    return render(request, 'about.html')

def listing_detail(request, listing_id):
    house_listing = HouseListing.objects.get(pk=listing_id)
    return render(request, 'listing_detail.html', {
        'house_listing': house_listing,
    })
