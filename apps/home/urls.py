from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('aloqa/', views.AloqaSendEmailView.as_view(), name='aloqa'),
    path('maintance/', views.MaintanceView.as_view(), name='maintance'),
    path('maktab_haqida/', views.MaktabHaqida.as_view(), name='maktab_haqida'),
    path('maktab_ramzi/', views.MaktabRamzi.as_view(), name='maktab_ramzi'),
    path('online_ariza/', views.SendEmail.as_view(), name='send_mail'),
    path('savollar/', views.Savollar.as_view(), name='savollar'),
    path('ota-onlar', views.FatherAndMotherListView.as_view(), name='fm_list'),
    path('ota-onlar/<str:slug>', views.FatherAndMotherDetailView.as_view(), name='fm_detail'),
]
