from django.urls import path
from schoolnews import views

app_name = 'schoolnews'


urlpatterns = [
    path('', views.index, name='index'),

    ]