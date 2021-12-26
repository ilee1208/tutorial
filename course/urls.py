from django.urls import path, include
from django.contrib import admin
from course import views


app_name='course'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courseHome/', views.courseHome, name='courseHome'),

    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('courseAdd/', views.courseAdd, name='courseAdd'),
    path('courseEdit/<int:course_id>/', views.courseEdit, name='courseEdit'),
    path('courseReform/<int:course_id>/', views.courseReform, name='courseReform'),
]
