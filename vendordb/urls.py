"""Defines URL patterns for vendordb."""

from django.urls import path

from . import views

app_name = 'vendordb'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all vendors
    path('vendors/', views.vendors, name='vendors'),

    # Detail page for a single vendor
    path('vendors/<int:vendor_id>/', views.vendor, name='vendor'),

    # Page for adding a new vendor
    path('new_vendor/', views.new_vendor, name='new_vendor'),
]
