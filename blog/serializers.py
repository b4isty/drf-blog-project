from rest_framework import serializers

from .models import Post, BlogImage, Comment


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
        read_only_fields = ['id', 'author']

    # def create(self, validated_data):
    # print("**", validated_data)
    #     blog_image = validated_data.pop('blog_image')
    #     post_obj = Post.objects.create(**validated_data)
    #     # post_obj.save()
    #     # post_obj.blog_image =


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment_text', 'post']
        read_only_fields = ['id', 'user']

    def to_representation(self, instance):
        representation = super(CommentsSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        representation['post'] = instance.post.title
        return representation

    # def create(self, validated_data):
    #     print("*****", validated_data)
    #     # return validated_data