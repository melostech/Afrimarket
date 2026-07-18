# core/permissions.py
from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    """
    Allows access only to users with the SELLER role.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role == 'SELLER')

class IsAdminUser(permissions.IsAdminUser):
    """
    Allows access only to users with the ADMIN role or staff status.
    """
    def has_permission(self, request, view):
        is_admin_role = bool(request.user and request.user.is_authenticated and hasattr(request.user, 'role') and request.user.role == 'ADMIN')
        return super().has_permission(request, view) or is_admin_role

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute. Adjust as necessary (e.g., `seller_id`, `buyer_id`).
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        # Check standard common owner fields
        if hasattr(obj, 'user'):
            return obj.user == request.user
        elif hasattr(obj, 'seller'):
            return hasattr(request.user, 'sellerprofile') and obj.seller == request.user.sellerprofile
        elif hasattr(obj, 'buyer'):
            return obj.buyer == request.user
            
        return False
