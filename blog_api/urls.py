from django.urls import path
from .views import PostList, PostDetail

app_name='blog_api'

urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(),name='detailcreate'), 
    path('',PostList.as_view(),name='listcreate'), 
]

#nb - the urls are reference to the api end points for post requests? no they are posts that are recieved from a get requst. . 
