from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
]