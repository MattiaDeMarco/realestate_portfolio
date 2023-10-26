from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage' ),
    path('gallery', views.gallery, name='gallery'),
    path('property/<str:pk>', views.property, name='property'),
    #path('upload', views.upload, name='upload'),
    path('test/<str:pk>', views.test, name='test'),
    path('photo/<str:pk>/', views.viewPhotos, name='photo')
]