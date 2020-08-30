from .serializer import (Blog, BlogComment, BlogTag,
                         BlogSerializer, BlogCommentSerializer, BlogTagSerializer)
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        query = self.request.query_params.dict()
        keyword = query.pop("keyword", None)
        query.pop("page", None)
        query_data = self.queryset
        if keyword:
            query_data = query_data.filter(
                Q(title__icontains=keyword) |
                Q(title__iexact=keyword) |
                Q(tags__title__icontains=keyword) |
                Q(tags__title__iexact=keyword)
            ).distinct()
        return query_data.filter(**query)


class BlogCommentView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

    def get_queryset(self):
        query = self.request.query_params.dict()
        query.pop("page", None)
        return self.queryset.filter(**query)


class BlogTagView(ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TopBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        blogs = self.queryset.annotate(comment_count=Count(
            'blog_comments')).order_by('-comment_count')[:5]
        return blogs


class SimilarBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_queryset(self):
        blog_id = self.kwargs.get("blog_id")
        try:
            blog_tags = self.queryset.get(id=blog_id).tags.all()
        except Exception:
            return []
        blogs = self.queryset.filter(
            tags__id__in=[tag.id for tag in blog_tags]).exclude(id=blog_id)[:5]
        return blogs
