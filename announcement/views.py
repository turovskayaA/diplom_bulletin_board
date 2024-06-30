from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny

from announcement.filter import AnnouncementFilter
from announcement.models import Adt, Review
from announcement.paginators import AnnouncementPaginator
from announcement.permissions import IsUser, IsAdmin
from announcement.serializers import AdtSerializers, ReviewSerializers


class AdtCreateApiView(CreateAPIView):
    """
    Создание объявление
    """

    serializer_class = AdtSerializers
    queryset = Adt.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        user.author = self.request.user
        user.save()


class AdtListApiView(ListAPIView):
    """
    Просмотр всех объявлений
    """

    serializer_class = AdtSerializers
    queryset = Adt.objects.all()
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnnouncementFilter
    pagination_class = AnnouncementPaginator


class AdtRetrieveApiView(RetrieveAPIView):
    """
    Просмотр конкретного объявление
    """

    serializer_class = AdtSerializers
    queryset = Adt.objects.all()
    permission_classes = [IsUser | IsAdmin]


class AdtUpdateApiView(UpdateAPIView):
    """
    Редактирование объявление
    """

    serializer_class = AdtSerializers
    queryset = Adt.objects.all()
    permission_classes = [IsUser | IsAdmin]


class AdtDestroyApiView(DestroyAPIView):
    """
    Удаление объявление
    """

    serializer_class = AdtSerializers
    queryset = Adt.objects.all()
    permission_classes = [IsUser | IsAdmin]


class ReviewCreateApiView(CreateAPIView):
    """
    Создание отзыва
    """

    serializer_class = ReviewSerializers
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        user.author = self.request.user
        user.save()


class ReviewListApiView(ListAPIView):
    """
    Просмотр отзыва
    """

    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [AllowAny]
    pagination_class = AnnouncementPaginator


class ReviewRetrieveApiView(RetrieveAPIView):
    """
    Просмотр конкретного отзыва
    """

    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [IsUser | IsAdmin]


class ReviewUpdateApiView(UpdateAPIView):
    """
    Редактирование отзыва
    """

    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [IsUser | IsAdmin]


class ReviewDestroyApiView(DestroyAPIView):
    """
    Удаление отзыва
    """

    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [IsUser | IsAdmin]
