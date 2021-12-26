from django.urls import path, include
from django.contrib import admin
from bootstrap import views


app_name='bootstrap'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bsHome/', views.bsHome, name='bsHome'),
    path('bsList/', views.bsList, name='bsList'),
    path('bsAdd/', views.bsAdd, name='bsAdd'),
    path('bsEdit/<int:bs_id>/', views.bsEdit, name='bsEdit'),
    path('bsReform/<int:bs_id>/', views.bsReform, name='bsReform'),
]
