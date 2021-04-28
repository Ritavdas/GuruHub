from django.shortcuts import render, redirect
from .models import Card, Subject, Tutor
from hashlib import sha1
from django.core.mail import send_mail
#from django.contrib import auth
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password

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
    category = request.POST['category']

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
            #User.objects.create(first_name=fn, last_name = ln, username = username, password = password,email = email)
            user = User.objects.create_user(first_name=fn, last_name = ln, username = username, password = password,email = email)
            user.save()

            if category == "tutor":
                Tutor(tid = int(Tutor.objects.all().count()) + 1, pic = None, name = fn, star = 0, about = "null", taught = 0, rate = 0, address = "null" ).save()
            return render(request, 'login.html',{'msg1':"Thanks for Registering with us."})

def loginload(request):
    return render(request,'login.html')


def logout(request):
    
    auth.logout(request)
    return render(request, 'index.html',{'msg1':"Successfully logged out!"})




def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html',{'msg1':"You are now logged in"})
        else:
            return render(request, 'login.html',{'msg2':"Invalid Credentials"})
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


from .models import Card

# Create your views here.
def index(request):
    car = Card.objects.all()
    return render(request, 'index.html', {'cards':car})


def maindash(request):

    return render(request, 'maindash.html')


def changepswd(request):
    return render(request, 'changepswd.html')

def pswdchanged(request):
    msg = ""



    old = request.POST['old']
    new = request.POST['new']
    connew = request.POST['connew']

    if old == "" or new=="" or connew=="":
        return render(request,'changepswd.html', {'msg':"Enter required fields!"})

    
    if new!=connew:
        return render(request,'changepswd.html', {'msg':"Password do not match!"})

    if check_password(old,User.objects.get(username = request.user.username).password):
        p = User.objects.get(username = request.user.username)
        p.password = make_password(new)
        p.save()
        send_mail('Password changed!', 'Hello ' + request.user.first_name + ", Your password has been changed successfully!", 'guruhubportal@gmail.com', [request.user.email],fail_silently=False)
        return render(request, 'pswdchanged.html', {'msg':"Password successfully changed! Mail sent to respective mailing address!"})
    else:
        return render(request,'changepswd.html', {'msg':"Old password do not match with our records!"})


def forgetpass(request):
    return render(request,'forgetpass.html')


def mailsent(request):

    username = request.GET['username']
    
    if User.objects.filter(username=username).exists():
        return render(request,'mailsent.html')

    else:
        return render(request,'forgetpass.html', {"msg":"User does not exist!"})

    
    




    
    


