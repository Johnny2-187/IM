from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customer_updateregpage/', views.customer_updateregpage, name='customer_updateregpage'),
    path('customer_profileinfopage/', views.customer_profileinfopage, name='customer_profileinfopage'),
    path('customer_updateregpage/', views.profile_information_page_view, name='profile_information_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
