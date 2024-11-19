from django.urls import path
from . import views


urlpatterns = [
    path('/registration/', views.registration_view ),
    path('/authorization/', views.authorization_view ),
    path('confirmation/', views.confirmation_view),

]