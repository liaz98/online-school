from django.urls import path
from .views import *

urlpatterns = [
    path('', tugarak_home, name='togarak_home'),
    path('<str:slug>/', TogarakDetail.as_view(), name='togarak_detail'),
    path('qoshimchadars/', qoshimchadars_home, name='qoshimchadars_home'),
    path('qoshimchadars/<str:slug>/', QoshimchaDarsDetail.as_view(), name='qoshimchadars_detail')
]