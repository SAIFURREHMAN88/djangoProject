from django.urls import path
from base import views
urlpatterns = [
    path('', views.home, name='home'),
    path ('your_view',views.your_view,name='your_view'),
]