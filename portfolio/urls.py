"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from charity_donation import views as chd_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', chd_views.LandingPage.as_view(), name="main"),
    path('login/', chd_views.Login.as_view(), name="login"),
    path('register/', chd_views.Register.as_view(), name="register"),
    path('AddDonation/', chd_views.AddDonation.as_view(), name="add_donation"),
    path('logout/', chd_views.UserLogout.as_view(), name="logout"),
    path('profil/', chd_views.UserPage.as_view(), name="profil"),
    path('form-confirmation/', chd_views.FormConfirmation.as_view(), name='form-confirmation'),



    path('AddInstitution/', chd_views.InstitutionCreate.as_view(), name="add_institution"),
    path('AddCategory/', chd_views.CategoryCreate.as_view(), name="add_institution"),
]
