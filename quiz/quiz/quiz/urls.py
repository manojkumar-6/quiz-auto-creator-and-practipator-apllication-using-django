"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("register.urls")),
    path("create",include("register.urls")),
    path("t/<str:g>",include("register.urls")),
    path("u/<str:i>",include("register.urls")),
    path("homes",include("register.urls")),
    path("update/<str:g>/<int:pk>",include("register.urls")),
    path("dele/<str:g>/<int:pk>",include("register.urls")),
    path("a/<str:g>/<str:acd>",include("register.urls")),
    path("delete/<str:p>",include("register.urls")),
    path("see/<str:xq>",include("register.urls")),
    path("reg",include("register.urls")),
    path("par",include("register.urls")),
    path("quiz/<str:g>",include("register.urls")),
    path("r",include("register.urls")),
]
