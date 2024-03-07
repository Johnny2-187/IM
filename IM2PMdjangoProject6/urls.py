
from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profileinfopage/', views.profileinfopage, name='profileinfopage'),


]
