from django.urls import path, include
from django.contrib import admin
from python import views


app_name='python'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pyHome/', views.pyHome, name='pyHome'),
    path('pyAdd/', views.pyAdd, name='pyAdd'),
    path('pyEdit/<int:py_id>/', views.pyEdit, name='pyEdit'),
    path('pyReform/<int:py_id>/', views.pyReform, name='pyReform'),
    path('pyTest/', views.pyTest, name='pyTest'),
]