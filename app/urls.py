from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('login',views.login_view,name='login'),
    path('signup',views.signup_view,name='signup'),
    path('logout',views.logout_view,name='logout'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('change_status/<int:id>/<str:status>',views.change_status)
    
]