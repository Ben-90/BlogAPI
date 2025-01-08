from django.urls import path, include 

from .views import PostList, PostDetail, PostCreate

urlpatterns = [
    path("",PostList.as_view(), name = "post_list" ),
    path("<int:pk>/", PostDetail.as_view(), name = "post_detail"),
    path('newPost/', PostCreate.as_view(), name = "new_post"),

]



