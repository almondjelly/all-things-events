from django.shortcuts import render, redirect

from .models import Vendor
from .forms import VendorForm


def index(request):
    """The home page for Learning Log."""
    return render(request, 'vendordb/index.html')


def vendors(request):
    """Show all vendors."""
    vendors = Vendor.objects.order_by('text')
    context = {'vendors': vendors}
    return render(request, 'vendordb/vendors.html', context)


def vendor(request, vendor_id):
    """Show a single vendor."""
    vendor = Vendor.objects.get(id=vendor_id)
    context = {'vendor': vendor}
    return render(request, 'vendordb/vendor.html', context)


def new_vendor(request):
    """Add a new vendor."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = VendorForm()
    else:
        # POST data submitted; process data.
        form = VendorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendordb:vendors')

    # Display a blank for invalid form.
    context = {'form': form}
    return render(request, 'vendordb/new_vendor.html', context)
