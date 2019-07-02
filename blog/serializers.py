from rest_framework import serializers
from .models import Post, BlogImage


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    blog_image = serializers.PrimaryKeyRelatedField(queryset=BlogImage.objects.all(), many=True)
    # blog_image = BlogImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'blog_image']
        read_only_fields = ['author', 'id']

    # def create(self, validated_data):
        # print("**", validated_data)
    #     blog_image = validated_data.pop('blog_image')
    #     post_obj = Post.objects.create(**validated_data)
    #     # post_obj.save()
    #     # post_obj.blog_image =


