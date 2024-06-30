from django.urls import path
from rest_framework.routers import DefaultRouter

from announcement.apps import AnnouncementConfig
from announcement.views import (
    AdtCreateApiView,
    AdtListApiView,
    AdtRetrieveApiView,
    AdtUpdateApiView,
    AdtDestroyApiView,
    ReviewCreateApiView,
    ReviewListApiView,
    ReviewRetrieveApiView,
    ReviewUpdateApiView,
    ReviewDestroyApiView,
)

app_name = AnnouncementConfig.name

# router = DefaultRouter()
# router.register(r"review", ReviewViewSet, basename="review")

urlpatterns = [
    path("adt/create/", AdtCreateApiView.as_view(), name="create"),
    path("adt/list/", AdtListApiView.as_view(), name="list"),
    path("adt/<int:pk>/", AdtRetrieveApiView.as_view(), name="get"),
    path("adt/update/<int:pk>/", AdtUpdateApiView.as_view(), name="update"),
    path("adt/delete/<int:pk>/", AdtDestroyApiView.as_view(), name="delete"),
    path("review/create/", ReviewCreateApiView.as_view(), name="review_create"),
    path("review/list/", ReviewListApiView.as_view(), name="review_list"),
    path("review/<int:pk>/", ReviewRetrieveApiView.as_view(), name="review_get"),
    path(
        "review/update/<int:pk>/", ReviewUpdateApiView.as_view(), name="review_update"
    ),
    path(
        "review/delete/<int:pk>/", ReviewDestroyApiView.as_view(), name="review_delete"
    ),
]
# + router.urls
