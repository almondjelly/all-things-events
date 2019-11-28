from django.shortcuts import render

from .models import Vendor


def index(request):
    """The home page for Learning Log."""
    return render(request, 'vendordb/index.html')


def vendors(request):
    """Show all vendors."""
    vendors = Vendor.objects.order_by('text')
    context = {'vendors': vendors}
    return render(request, 'vendordb/vendors.html', context)
