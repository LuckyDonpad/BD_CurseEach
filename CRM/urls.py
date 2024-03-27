"""
URL configuration for CRM project.

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
from website.views import *

urlpatterns = [
    path('logout', logout_view, name="logout"),
    path('', auth, name="auth"),
    path('admin/', admin.site.urls),
    path('auth/', auth, name="auth"),
    path('add_client/', add_client),
    path('backup/', backup),
    path('create_task/', create_task),
    path('current_tasks/', current_tasks),
    path('view_client/', view_client),
    path('view_worker/', view_worker),
    path('add_worker/', add_worker),
    path('failed_tasks/', failed_tasks),
    path('change_worker/<pk>', change_worker),
    path('change_client/<pk>', change_client),
    path('change_task/<pk>', change_task),

]
