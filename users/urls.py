from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from users.apps import UsersConfig

app_name = UsersConfig.name
users_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    # path('auth/', include('djoser.urls')),  # auth/jwt/create/ - Получение JWT-токена
    path("token/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
