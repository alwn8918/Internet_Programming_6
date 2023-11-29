from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

app_name = "login"
urlpatterns = [
    #path('', views.login),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


#return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))