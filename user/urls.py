from .views import UserView, GenericFileView, MarkettingView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register("users", UserView)
router.register("file-upload", GenericFileView)
router.register("marketting", MarkettingView)

urlpatterns = [
    path('', include(router.urls))
]
