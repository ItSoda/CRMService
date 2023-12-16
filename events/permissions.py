from rest_framework.permissions import BasePermission



class IsCreatorUser(BasePermission):
    """
    Allows access only to creator users.
    """

    def has_permission(self, request, view):
        return bool(request.user and [role for role in request.user.users_roles if role in ("creator", "admin")])