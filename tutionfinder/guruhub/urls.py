from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),

    path('login',views.loginload),
    path('dashboard',views.login),
    path('result',views.regres),
    path('logout',views.logout),
    path('maindash', views.maindash),

    path('searchresults', views.searchresults)
]
