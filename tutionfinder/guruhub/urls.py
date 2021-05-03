from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.loginload),
    path('dashboard', views.login),
    path('result', views.regres),
    path('logout', views.logout),
    path('maindash', views.maindash),
    path('changepswd', views.changepswd),
    path('pswdchanged', views.pswdchanged),
    path('forgetpass', views.forgetpass),
    path('mailsent', views.mailsent),
    path('personaldetails', views.personaldetails),
    path('detailsadded', views.detailsadded),
    path('addsubject', views.addsubject),
    path('subjectadded', views.subjectadded),
    path('booktutor', views.booktutor),
    path('givestar', views.givestar),


    path('searchresults', views.searchresults)

]
