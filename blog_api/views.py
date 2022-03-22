#createviews- class based views for postlist and postdetail. 
from rest_framework import generics
from blog.models import Post
from.serializers import PostSerializer

class  PostList(generics.ListCreateAPIView): 
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass 
