from django.urls import path
from . import views

urlpatterns = [
    path('bolalar-kitoblari/', views.ChildrenBookListView.as_view(), name='book'),
    path('electron', views.ElectronListView.as_view(), name='electron_list'),
    path('electron/<str:slug>', views.ElectronDetailView.as_view(), name='electron_detail'),
    path('video', views.VideoListView.as_view(), name='video_list'),
    path('video/<str:slug>', views.VideoDetailView.as_view(), name='video_detail'),
]
