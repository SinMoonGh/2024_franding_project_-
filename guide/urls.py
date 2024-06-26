# guide/urls.py

from django.contrib import admin
from django.urls import path
from guide import views

app_name = 'guide'  # 네임스페이스 설정

urlpatterns = [
    path('', views.guide_list, name='guide_list'),
    path('brandstory/', views.brand_story, name='brand Story'),
    path('description/', views.description, name='description'),
    path('pleasant/', views.pleasant, name='pleasant'),
    path('scent/', views.scent, name='scent'),
    path('tale/', views.tale, name='tale'),
    path('tip/', views.tip, name='tip'),
]
