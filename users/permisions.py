from rest_framework.permissions import BasePermission
from users.api import UserDetailAPI

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Define si el usuario autenticado en request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        """
        # Si quiere crear un usuario, sea quien sea puede
        if request.method == "POST":
            return True
        # si no es POST, el superusario siempre puede
        elif request.user.is_superuser:
            return True
        # si es un GET a la vista de detalle, tomo la decisión en has_object_permissions
        elif isinstance(view, UserDetailAPI):
            return True        
        else:
            # GET a /api/1.0/users/
            False

    def has_object_permission(self, request, view, obj):
        """
        Define si el usuario autenticado enr request.user tiene
        permiso para realizar la acción (GET, POST, PUT o DELETE)
        sobre el object obj
        """
        pass