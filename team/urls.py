from django.urls import path
from . import views


urlpatterns = [
    path('', views.content),
    path('', views.TeamList.as_view()),
    path('filter/', views.team_view),

    path('<int:pk>/', views.DetailContentView.as_view()),
    path('<int:pk>/', views.base_detail_content),
    path('<int:pk>/new_comment/', views.new_comment),

    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view()),
    path('delete_post/<int:pk>', views.PostDelete.as_view()),

    path('search/<str:q>/', views.TeamSearch.as_view()),
]