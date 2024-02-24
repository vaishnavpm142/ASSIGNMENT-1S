"""
URL configuration for project project.

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

# Importing necessary modules
from django.contrib import admin
from django.urls import path
from app import views

# URL patterns mapping to views
urlpatterns = [
    path('home', views.home, name='home'),  # Home page URL
    path('admin/', admin.site.urls),  # Admin URL
    path('signup/', views.signup, name='signup'),  # Signup page URL
    path('signup/signupaction', views.signupaction, name='signupaction'),  # Signup action URL
    path('', views.login, name='login'),  # Login page URL
    path('loginaction', views.loginaction, name='loginaction'),  # Login action URL
    path('logout', views.custom_logout, name='custom_logout'),  # Logout URL
    path('approveuser/logout', views.custom_logout, name='custom_logout1'),  # Logout for approving user URL
    path('editlogin/<str:username>', views.editlogin, name='editlogin'),  # Edit login URL
    path('updatelogin/<int:id>', views.updatelogin, name='updatelogin'),  # Update login URL
    path('deletelogin/<int:id>', views.deletelogin, name='deletelogin'),  # Delete login URL
    path('editprofile', views.editprofile, name='editprofile'),  # Edit profile URL
    path('updateprofile', views.updateprofile, name='updateprofile'),  # Update profile URL
    path('changepassword', views.changepassword, name='changepassword'),  # Change password URL
    path('updatepassword', views.updatepassword, name='updatepassword'),  # Update password URL
    path('validateuser', views.validateuser, name='validateuser'),  # Validate user URL
    path('approveuser/<str:username>', views.approveuser, name='approveuser'),  # Approve user URL
    path('rejectuser/<str:username>', views.rejectuser, name='rejectuser'),  # Reject user URL
    path('editusers', views.editusers, name='editusers'),  # Edit users URL
    path('profilebase/', views.profilebase, name="profilebase"),  # Profile base URL
]
