from django.shortcuts import render
from  .models import Listing


def listing_list(request):
    listings = Listing.objects.all()

    # Context  is the python dictionary of data to inject inside HTML file
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)
