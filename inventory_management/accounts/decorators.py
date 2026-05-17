from django.shortcuts import redirect
from django.http import HttpResponse


def role_required(allowed_roles=[]):

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:

                return redirect('/login/')

            if request.user.role in allowed_roles:

                return view_func(
                    request,
                    *args,
                    **kwargs
                )

            return HttpResponse(
                "You are not authorized to access this page."
            )

        return wrapper

    return decorator