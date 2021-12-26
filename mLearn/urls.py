from django.urls import path, include
from django.contrib import admin
from mLearn import views


app_name='mLearn'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mLearnHome/', views.mLearnHome, name='mLearnHome'),
    path('mLearnAdd/', views.mLearnAdd, name='mLearnAdd'),
    path('mLearnEdit/<int:mLearn_id>/', views.mLearnEdit, name='mLearnEdit'),
    path('mLearnReform/<int:mLearn_id>/', views.mLearnReform, name='mLearnReform'),
    path('exHome/', views.exHome, name='exHome'),
    path('download/', views.download, name='download'),
    path('beautifulSoup/', views.beautifulSoup, name='beautifulSoup'),
    path('pandas/', views.pandas, name='pandas'),
    path('select/', views.select, name='select'),
    path('path/', views.path, name='path'),
    path('login/', views.login, name='login'),
    path('weather/', views.weather, name='weather'),
    path('selenium/', views.selenium, name='selenium'),
    path('mysql/', views.mysql, name='mysql'),
    path('datatype/', views.datatype, name='datatype'),
    path('jsontype/', views.jsontype, name='jsontype'),
    path('xmltype/', views.xmltype, name='xmltype'),
    path('csvtype/', views.csvtype, name='csvtype'),
    path('excel/', views.excel, name='excel'),
    path('plot/', views.plot, name='plot'),
    path('image/', views.image, name='image'),
    path('scikit/', views.scikit, name='scikit'),
    path('mLearnTest/', views.mLearnTest, name='mLearnTest'),
    path('conversion/', views.conversion, name='conversion'),
    path('lang/', views.lang, name='lang'),
    path('langTest/', views.langTest, name='langTest'),
    path('fat/', views.fat, name='fat'),
    path('mushroom/', views.mushroom, name='mushroom'),
    path('tensor/', views.tensor, name='tensor'),
    path('mnist/', views.mnist, name='mnist'),


]