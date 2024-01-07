from rest_framework import serializers

from ads.models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.CharField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    ad_id = serializers.CharField(source='ad.id', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk', 'text', 'author_id', 'created_at',
            'author_first_name', 'author_last_name',
            'ad_id', 'author_image'
        )


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description')


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    author_id = serializers.CharField(source='author.id')

    class Meta:
        model = Ad
        fields = (
            'pk', 'image', 'title', 'price', 'phone',
            'description', 'author_first_name', 'author_last_name', 'author_id'
        )

    def get_author_first_name(self, obj):
        return obj.author.first_name

    def get_author_last_name(self, obj):
        return obj.author.last_name

    def get_phone(self, obj):
        return obj.author.phone
