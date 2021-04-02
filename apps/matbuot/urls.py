from django.urls import path
from .views import *


urlpatterns = [
    path('', baseview, name='matbuot'),
    path('yangiliklar/', YangilikView.as_view(), name='yangiliklar'),
    path('biz-haqimizda/', OMVListView.as_view(), name='omv'),
    path('biz-haqimizda/<str:slug>', OMVDetailView.as_view(), name='omv_detail'),
    path('yangiliklar/<str:slug>', YangilikDetail.as_view(), name='yangilik_detail'),
    path('kategoriya/<str:slug>', KategoriyaList.as_view(), name='yangilik_kategoriya'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('gallery/<str:title>', CategoryImageList.as_view(), name='gallery_detail'),
]
