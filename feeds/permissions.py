from rest_framework.permissions import BasePermission

class CanViewFeedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('feeds.view_feed')

class CanAddFeedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('feeds.add_feed')

class CanChangeFeedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('feeds.change_feed')

class CanDeleteFeedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('feeds.delete_feed')