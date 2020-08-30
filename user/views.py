from .serializer import (User, UserSerializer,
                         GenericFileUpload, GenericFileSerializer, MarkettingSerializer, Marketting, MarkettingBanners)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GenericFileView(ModelViewSet):
    queryset = GenericFileUpload.objects.all()
    serializer_class = GenericFileSerializer


class MarkettingView(ModelViewSet):
    queryset = Marketting.objects.all()
    serializer_class = GenericFileSerializer
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
