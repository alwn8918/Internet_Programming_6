from django.urls import path
from . import views


urlpatterns = [
    path('', views.content),
    path('', views.base_content),
    path('<int:pk>/', views.DetailContentView.as_view()),
    path('<int:pk>/', views.base_detail_content),
]