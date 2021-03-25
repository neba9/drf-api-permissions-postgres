from rest_framework import permissions
import rest_framework

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.purchaser is None:
            return True

        return obj.purchaser == request.user








# from rest_framework import permissions
# import rest_framework

# class IsOwnerOrReadOnly(permissions.BasePermission):
#   def has_object_permission(self, request, views, obj):
#     if request.method in permissions.SAFE_METHODS:
#       return True

#     if obj.purchaser is None:
#       return True

#     return obj.purchaser == request.User
