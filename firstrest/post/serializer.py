from .models import Post
from rest_framework import serializers

# 7m 부터 다시

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # field = '__all__'
        fields = ['id','title', 'body']
        # read_only_fields = ('title',)
        write_only_fields = ('body',)
