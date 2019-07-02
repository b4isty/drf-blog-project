from rest_framework import permissions


class IsOwnerOrReadonly(permissions.BasePermission):
    """
    Create  permission to only allow owner of an object to edit and delete it.

    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
