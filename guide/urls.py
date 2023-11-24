from django.urls import path
from . import views

urlpatterns = [
    path('', views.GuideList.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('tagtype/<str:slug>/', views.tagtype_page),
    path('tagteam/<str:slug>/', views.tagteam_page),
]