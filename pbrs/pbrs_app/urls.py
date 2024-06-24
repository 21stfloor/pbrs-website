from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', views.listings, name='listings'),
    path('about/', views.about, name='about'),
    path('listings/<int:listing_id>/', views.listing_detail, name='listing_detail'),
]