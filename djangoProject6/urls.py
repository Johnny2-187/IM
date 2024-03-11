"""
URL configuration for djangoProject6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from IM2PMdjangoProject6 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('IM2PMdjangoProject6.urls')),
    path('admin/', admin.site.urls),
    path('customer_updateregpage/', views.customer_updateregpage, name='customer_updateregpage'),
    path('customer_profileinfopage/', views.customer_profileinfopage, name='customer_profileinfopage'),
    path('customer_updateregpage/', views.profile_information_page_view, name='profile_information_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout URL pattern
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
