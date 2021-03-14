from django.shortcuts import render
from .models import Card, Subject, Tutor

# Create your views here.
def index(request):
    car = Card.objects.all()
    return render(request, 'index.html', {'cards':car})



def searchresults(request):

    sub = request.GET['subjects']
    level = request.GET['level']
    addr = request.GET['location']

   

    try:
        mode = bool(request.GET['mode'])
        mode = 'In Person'

    except:
        mode = 'Online'

 
    results = Subject.objects.filter(subject__icontains = sub, level__icontains = level, mode__icontains = mode).select_related('tid')

    

    

    return render(request, 'searchresults.html',{'results':results})
