from django.urls import path
from . import views


urlpatterns = [
    path('', views.content),
    path('<int:pk>/', views.DetailContentView.as_view()),

    path('<int:pk>/new_comment/', views.new_comment),

    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view()),
    path('delete_post/<int:pk>', views.PostDelete.as_view()),

    path('main_category/<str:slug>/', views.MainCategory_page),
    # path('sub_category/<str:slug>/', views.get_subcategories),
    # path('sub_category/<str:slug>/', views.SubCategory_page),
    path('<str:main_slug>/sub_category/<str:slug>/', views.SubCategory_page),
]