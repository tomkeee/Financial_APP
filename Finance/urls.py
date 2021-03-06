"""Finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from portfolio.views import portfolio_view,region_view,sector_view,calculator
from profiles.views import login_view,logout_view,register_view
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from profiles.views import login_view,logout_view,UserEditView,PasswordsChangeView

urlpatterns = [
    path("blog/",include('blogpage.urls')),
    path('investment/',include('data.urls')),
    path("instrument/",include("instrument.urls")),

    path('admin/', admin.site.urls),
    path('register/',register_view),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name="logout"),
    path('edit/',UserEditView.as_view(),name="edit"),
    path('password/',PasswordsChangeView.as_view(template_name='registration/changePassword.html')),

    path('calculator/',calculator,name="calculator"),
    path('',portfolio_view,name='portfolio'),
    path('region/',region_view,name="region"),
    path('sector/',sector_view,name="sector"),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)