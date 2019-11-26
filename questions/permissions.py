from rest_framework import permissions

from django.contrib.auth.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user == User.objects.get(pk='1')
        )
