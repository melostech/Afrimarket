from rest_framework.permissions import BasePermission

#allow access only to seller
class IsSeller(BasePermission):
   def has_permission(self, request, view):
      return  (
         request.user.is_authenticated
         and request.user.role == "SELLER"
      )


#allow access only to buyers
class IsBuyer(BasePermission):
   def has_permission(self, request, view):
      return (
         request.user.is_authenticated
         and request.user.role == "BUYER"
      )


#allow access only to admins
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
      return (
         request.user.is_authenticated
         and request.user.role == "ADMIN"
      )