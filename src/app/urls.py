from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.conf.urls import include,url

app_name = 'app'
urlpatterns = [
    path('', views.FirstIndexView.as_view(), name='index'),
    path('list', views.IndexView.as_view(), name='list'),
    path('genre', views.GenreView.as_view(), name='genre'),
    path('list/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
