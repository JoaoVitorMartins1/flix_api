from rest_framework import permissions


class ReviewPermissionsClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.has_perm('reviews.add_review')
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('reviews.view_review')
        if request.method in ['PATCH', 'PUT']:
            return request.user.has_perm('reviews.change_review')
        if request.method == 'DELETE':
            return request.user.has_perm('reviews.delete_review')
        return False
