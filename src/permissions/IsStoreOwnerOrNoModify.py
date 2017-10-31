from rest_framework import permissions


class IsStoreOwnerOrNoModify(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        try:
            return not request.user.store
        except:
            # Write permissions are only allowed to the owner of the store.
            return obj.user == request.user
