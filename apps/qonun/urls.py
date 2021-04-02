from django.urls import path
from . import views

urlpatterns = [
    path('', views.Qonunlar, name='normativ'),
    path('ntm-faoliyati/', views.Normativs.as_view(), name='normativ'),
    path('maktab-qoidalari/', views.Qoidalar.as_view(), name='maktab_qoidalari'),
    path('shartnoma/', views.DownloadContractFile.as_view(), name='file'),
    path('uzbekistan/', views.UzbekistanView.as_view(), name='uzb'),
]
