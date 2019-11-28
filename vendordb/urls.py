"""Defines URL patterns for vendordb."""

from django.urls import path

from . import views

app_name = 'vendordb'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all vendors
    path('vendors/', views.vendors, name='vendors'),
]
