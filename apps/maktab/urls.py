from django.urls import path
from .views import *

urlpatterns = [
    path('sinflar/', Sinflar.as_view(), name='sinflar'),
    path('sinflar/<str:slug>', SinfDetail.as_view(), name='sinf_detail'),
    path('sinflar/yangiliklar/<str:slug>', SinfYangilikDetail.as_view(), name='sinf_yangilik_detail'),
    path('jadval/', Jadval.as_view(), name='jadval'),
    path('oqituvchi/', TeacherList.as_view(), name='oqituvchilar'),
    path('kun_tartibi/', KunTartibiList.as_view(), name='kun_tartibi'),
    path('oshxona/', KitchenListView.as_view(), name='kitchen'),
    path('taomnoma/<int:pk>', KitchenDetailView.as_view(), name='kitchen_detail'),
    path('tolmas_choy/', ChoyListView.as_view(), name='choy'),
    path('tolmas_choy/<int:pk>', ChoyDetailView.as_view(), name='choy_detail'),
    path('jarayoni/', JarayonListView.as_view(), name='jarayon_list'),
    path('jarayoni/<str:slug>', JarayonDetail.as_view(), name='jarayon_detail'),
]
