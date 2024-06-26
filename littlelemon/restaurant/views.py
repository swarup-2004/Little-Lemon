from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, "index.html", {})

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

