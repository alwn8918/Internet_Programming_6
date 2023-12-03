from django.urls import path
from . import views

app_name = "main_page"
urlpatterns = [
    path('', views.GuideList.as_view()),
    path('calendar/', views.calendar),
]