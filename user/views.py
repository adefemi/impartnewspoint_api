from .serializer import (User, UserSerializer,
                         GenericFileUpload, GenericFileSerializer, MarkettingSerializer, Marketting, MarkettingBanners)
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get(self, request):
        return Response(self.serializer_class(request.user).data)


class GenericFileView(ModelViewSet):
    queryset = GenericFileUpload.objects.all()
    serializer_class = GenericFileSerializer


class MarkettingView(ModelViewSet):
    queryset = Marketting.objects.all()
    serializer_class = MarkettingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, req, *args, **kwargs):
        banners = req.data.pop("banners", None)
        serializer = self.serializer_class(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if banners:
            MarkettingBanners.objects.bulk_create([MarkettingBanners(
                marketting_id=serializer.data["id"], banner=banner) for banner in banners])

        return Response(serializer.data, status=201)

    def update(self, req, *args, **kwargs):
        banners = req.data.pop("banners", None)
        instance = self.get_object()
        serializer = self.serializer_class(
            data=req.data, instance=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if banners:
            MarkettingBanners.objects.filter(
                marketting_id=instance.id).delete()
            MarkettingBanners.objects.bulk_create([MarkettingBanners(
                marketting_id=serializer.data["id"], banner=banner) for banner in banners])

        return Response(serializer.data)
