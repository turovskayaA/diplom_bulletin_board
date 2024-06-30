from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        is_authenticated = request.user.is_authenticated
        author = obj.author == request.user
        return author and is_authenticated


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin
