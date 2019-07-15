from  rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Create permissions to only allow owner of an object to accept and ignore
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
