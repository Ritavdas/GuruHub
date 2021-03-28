from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
    path('login',views.loginload),
    path('dashboard',views.login),
    path('result',views.regres),
=======
>>>>>>> 631264b5928366e9451d4ab12b2205b71b744e22
    path('searchresults', views.searchresults)
]
