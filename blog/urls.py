from django.urls import path, include
from .views import (BlogView, BlogCommentView,
                    BlogTagView, TopBlogs, SimilarBlogs, )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blogs', BlogView)
router.register('blog-tags', BlogTagView)
router.register('blog-comments', BlogCommentView)

urlpatterns = [
    path('', include(router.urls)),
    path('top-blogs', TopBlogs.as_view()),
    path('similar-blogs/<int:blog_id>', SimilarBlogs.as_view())
]
