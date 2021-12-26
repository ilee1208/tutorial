from django.urls import path, include
from django.contrib import admin
from main import views

app_name='main'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    path('logout/', views.logout, name='logout'),

]