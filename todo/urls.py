from django.urls import path
from . import views


urlpatterns = [
    path('today_page', views.today_page_view, name='today_page'),
]