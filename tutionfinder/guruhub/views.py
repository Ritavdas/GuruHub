from django.shortcuts import render, redirect
from .models import Card, Subject, Tutor, Book
from hashlib import sha1
import string
from django.core.mail import send_mail
from .forms import TutorCreate
import random
import shutil
import os
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

    results = Book.objects.filter(tutor__icontains = request.user.first_name)

    return render(request, 'maindash.html',{"res":results})


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

    pwds = ['1234', 'samarth', 'capstone', '1111', 'mypassword','hello']

    
  

    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = 5))
  


    r = random.randint(0,len(pwds)-1)



    username = request.GET['username']
    
    if User.objects.filter(username=username).exists():
        email = User.objects.get(username = username).email
        p = User.objects.get(username = username)
        p.password = make_password(str(res))
        p.save()
        send_mail('Password changed!', 'Hello ' + username + ", Your new password is "+"'"+str(res)+"'", 'guruhubportal@gmail.com', [email],fail_silently=False)
        return render(request,'mailsent.html')

    else:
        return render(request,'forgetpass.html', {"msg":"User does not exist!"})


def personaldetails(request):


        
    return render(request,'personaldetails.html')


def detailsadded(request):

    profilepic = request.GET['profilepic']

    
    path = os.path.join("E:\SEMVI\Capstone-I\photos",str(profilepic))
    shutil.copy(path, "E:/SEMVI/Capstone-I/GuruHub/tutionfinder/media/pics")

    

    about = request.GET['about']
    rate = request.GET['rate']
    address = request.GET['address']
    
    p = Tutor.objects.get(name = request.user.first_name)


    p.pic = "pics/" + str(profilepic)
    p.about = about
    p.rate = rate
    p.address = address

    p.save()

    return render(request,'personaldetails.html', {"msg":"Details successfully added!"})

def addsubject(request):

    return render(request,'addsubject.html')


def subjectadded(request):

    subject = request.GET['subject']
    subjectlevel = request.GET['subjectlevel']
    mode = request.GET['mode']

    tid_id = Tutor.objects.get(name = request.user.first_name).tid

    Subject.objects.create(id = int(Subject.objects.all().count()) + 1 ,subject=subject, level=subjectlevel, mode=mode, tid_id = tid_id)


    #return render(request,'addsubject.html',{"msg":"Subject added successfully!"})
    return render(request,'addsubject.html',{"msg":tid_id})


def booktutor(request):

    tutor = request.GET['name']

    try:

        student = request.user.first_name
    except:
        return render(request,'booktutor.html',{"msg":"Please login as student first!"})


    Book.objects.create(tutor = tutor, student = student)

    return render(request,'booktutor.html')



def givestar(request):

    if request.user.is_authenticated:

        name = request.GET['name']

        try:
            star = int(request.GET['givestar'])
        except:
            return render(request,'searchresults.html',{"starmsg":"Go back and enter the starrating or give rating only in integer!"})

        
        if isinstance(star, int) and star<=5:
            starobj = Tutor.objects.get(name = name)
            starobj.starcount = starobj.starcount + 1

            starobj.save()
            #print("Hello")

            starobj = Tutor.objects.get(name = name)

            
            b = (  (starobj.star*(int(starobj.starcount)-1))   + star)/int(starobj.starcount)
            starobj.star = round(b,1)
            starobj.save()
            return render(request,'searchresults.html',{"starmsg":"Star rating given!"})



        else:
            return render(request,'searchresults.html',{"starmsg":"Enter rating between 1 to 5 only!"})



            


    else:
        return render(request,'searchresults.html',{"starmsg":"To give rating, you first need to login!"})
    

    
    




    
    


