from rest_framework import serializers

from .models import Post, BlogImage, Comment, Like


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    blog_image = serializers.PrimaryKeyRelatedField(queryset=BlogImage.objects.all(), many=True)
    comment = serializers.SerializerMethodField(read_only=True)
    like = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'blog_image', 'comment', 'like']
        read_only_fields = ['author', ]

    def get_comment(self, obj):
        qs = Comment.objects.filter(post__id=obj.id)
        serializer = CommentsSerializer(qs, many=True)
        return serializer.data

    def get_like(self, obj):
        qs = Like.objects.filter(post__id=obj.id)
        print("&&&&&&&&", qs)
        serializer = LikeSerializer(qs, many=True)
        return serializer.data


class PostSerializer(serializers.ModelSerializer):
    # blog_image = BlogImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'blog_image']
        read_only_fields = ['author', ]


class CommentsSerializer(serializers.ModelSerializer):
    # post = PostSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment_text', 'post']
        read_only_fields = ['user', ]

    def to_representation(self, instance):
        representation = super(CommentsSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        representation['post'] = instance.post.title
        return representation

    # def create(self, validated_data):
    #     print("*****", validated_data)
    #     # return validated_data


# class PostCommentSerializer(serializers.ModelSerializer):
#     post = PostSerializer()
#
#     class Meta:
#         model = Comment
#         fields = ['id', 'user', 'comment_text', 'post']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['user', ]

    # def create(self, validated_data):
    #     print("*****", validated_data)
    #     obj, created = Like.objects.get_or_create(**validated_data)
    #     return obj

