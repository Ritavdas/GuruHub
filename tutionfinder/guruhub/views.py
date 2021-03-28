from django.shortcuts import render
from .models import Card, Subject, Tutor
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    car = Card.objects.all()
    return render(request, 'index.html', {'cards':car})


def regres(request):

    fn = request.POST['first_name']
    ln = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password1']
    confirm_password = request.POST['password2']

    if fn=="" or username=="" or email=="" or password=="" or confirm_password=="":

        return render(request, 'index.html',{'msg':"Please fill required field!"})

       
    if password != confirm_password:
        return render(request, 'index.html',{'msg':'Password do not match!'})
    if User.objects.filter(username=username).exists():
        return render(request, 'index.html',{'msg':'Username already Exists!'})

    else:
        if User.objects.filter(email=email).exists():
            return render(request, 'index.html',{'msg':'Email already Exists!'})

        else:
            #Looks good
            User.objects.create(first_name=fn, last_name = ln, username = username, password = password,email = email)
            return render(request, 'index.html',{'msg1':"Thanks for Registering with us."})

def loginload(request):
    return render(request,'login.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard.html',{'msg1':"You are now logged in"})
        else:
            return render(request, 'index.html')
    else:
        return render(request,'login.html')


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


