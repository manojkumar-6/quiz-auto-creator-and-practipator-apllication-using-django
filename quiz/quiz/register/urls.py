from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("reg",views.reg,name="reg"),
    path("homes",views.homes,name="homes"),
    path("r",views.r,name="h"),
    path("par",views.par,name="par"),
    path("create",views.create,name="create"),
    path("t/<str:g>",views.t,name="t"),
    path("delete/<str:p>",views.delete,name="del"),
    path("u/<str:i>",views.u,name="u"),
    path("see/<str:xq>",views.sees,name="sees"),
    path("quiz/<str:g>",views.quiz,name="quiz"),
    path("update/<str:g>/<int:pk>",views.update,name="fg"),
    path("dele/<str:g>/<int:pk>",views.dele,name="fd"),
    path("a/<str:g>/<str:acd>",views.analyse,name="fdhg"),
    path("accounts/",include("django.contrib.auth.urls")),
]
