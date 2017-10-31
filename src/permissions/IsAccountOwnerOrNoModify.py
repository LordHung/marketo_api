from rest_framework import permissions


class IsAccountOwnerOrNoModify(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method.lower() in ['post', 'get', 'head', 'option', ]:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        try:
            return obj.email == request.user.email
        except:
            pass
