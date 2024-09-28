from django.urls import path
from . import views

urlpatterns = [
    path('',views.newshome, name='newshome'),
    path('create',views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='newsdetail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='newsupdate'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='newsdelete')
]
