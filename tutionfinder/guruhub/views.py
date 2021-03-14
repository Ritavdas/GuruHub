from django.shortcuts import render
from .models import Card
# Create your views here.
def index(request):
    car = Card.objects.all()
    return render(request, 'index.html', {'cards':car})



def searchresults(request):

    return render(request, 'searchresults.html')
