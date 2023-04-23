from django.core.exceptions import PermissionDenied


def user_is_seller(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'seller':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_buyer(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'buyer':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap