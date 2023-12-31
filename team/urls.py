from django.urls import path
from . import views


urlpatterns = [
    path('', views.content),
    path('', views.base_content),
    path('filter/', views.filtered_content),

    path('category/<str:slug>/', views.get_main_category_posts),
    path('category/<str:slug_main>/<str:slug_sub>', views.get_sub_category_posts),

    path('<int:pk>/', views.DetailContentView.as_view()),
    path('<int:pk>/', views.base_detail_content),
    path('<int:pk>/new_comment/', views.new_comment),

    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view()),
    path('delete_post/<int:pk>', views.PostDelete.as_view())
]