from rest_framework import serializers
from blog.models import Post 

#serializers allow data to be translated into a form tha is easily rendered into JSON or XML- 
class PostSerializer (serializers.ModelSerializer):
    class Meta:
        model= Post
        fields=('id','title','author','excerpt','content','status')