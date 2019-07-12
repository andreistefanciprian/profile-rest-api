from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to use their own profile"""
        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update their own status"""
        if request.method is permissions.SAFE_METHODS:
            return True
        # if feed item's user_profile same as logged user return True and allow user to update status
        # otherwise return False and forbid user
        return obj.user_profile.id == request.user.id