from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City that never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700

    dest2 = Destination()
    dest2.name = 'New York'
    dest2.desc = 'Manhattan is the spot'
    dest2.img = 'destination_2.jpg'
    dest2.price = 900

    dest3 = Destination()
    dest3.name = 'Haiti'
    dest3.desc = 'Go to Capital'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1100

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})

