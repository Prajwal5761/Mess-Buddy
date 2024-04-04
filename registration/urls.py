"""
URL configuration for registration project.

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
from django.urls import path
from django.contrib.auth.decorators import login_required
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Signup_LoginPage, name='signup'),
    path('about/', views.AboutPage, name='about'),
    path('contact/', views.ContactPage, name='contact'),
    path('dashboard/menu/', views.MenuPage, name='menu'),
    path('dashboard/menu/total_amt/', views.TotalAmt, name='breakfast_amt'),
    path('dashboard/', login_required(views.DashPage), name='dashboard'),
    path('logout/', views.LogoutPage, name='logout'),
    path('dashboard/lunch/', views.LunchPage, name='lunch'),
    path('dashboard/lunch/total_plates/', login_required(views.TotalPlates), name='total_plates'),
    path('dashboard/user_data/', login_required(views.GetData), name='user_data'),
    path('profiles/', views.profile_listPage, name='profile_list'),
    path('bill/', views.BillPage, name='bill_page'),
    path('total_bill/', views.TotalBillPage, name='total_bill'),
]
