from rest_framework.permissions import BasePermission

class CanViewCommentaryPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('commentary.view_commentary')

class CanAddCommentaryPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('commentary.add_commentary')

class CanChangeCommentaryPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('commentary.change_commentary')

class CanDeleteCommentaryPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('commentary.delete_commentary')