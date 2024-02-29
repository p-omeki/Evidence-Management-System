# decorators.py
from django.shortcuts import redirect
from django.contrib import messages

def guest_required(view_func):
    """
    decorator that ensures only guest users can access a page
    """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # User is not authenticated (guest user), allow access to the view.
            return view_func(request, *args, **kwargs)
        else:
            # User is authenticated as an officer, redirect to the home view.
            messages.error(
                request,
                "You are already logged in as an officer. If you want to access this page, please log out first.",
            )
            return redirect(
                "user_app:home"
            )  # Replace with the actual URL name of the home view.

    return wrapper

def itofficer_required(view_func):
    """
    decorator that ensures only it officers can access a page
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_itofficer:
                # User is authenticated and is an IT officer, allow access to the view.
                return view_func(request, *args, **kwargs)
            elif request.user.is_ocs:
                # User is authenticated but is an ocs, redirect to the home view.
                messages.error(
                    request,
                    "Only IT officers are allowed to access this page. If you are an IT, please log in with your account.",
                )
                return redirect(
                    "user_app:home"
                )  # Replace with the actual URL name of the home view.
            elif request.user.is_duty_officer:
                # User is authenticated but is a duty officer, redirect to the homepage view.
                messages.error(
                    request,
                    "Only IT officers are allowed to access this page. If you are an IT, please log in with your account.",
                )
                return redirect(
                    "user_app:home"
                )  # Replace with the actual URL name of the home view.
        else:
            # User is not authenticated, redirect to the login view.
            messages.error(
                request,
                "You need to log in as an IT officer to access this page. If you do not have an account, please contact IT support for further assistance.",
            )
            return redirect(
                "login"
            )  # Replace with the actual URL name of the login view.

    return wrapper


def ocs_required(view_func):
    """
    decorator that ensures only ocs can access a page
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_ocs:
                # User is authenticated and is an OCS, allow access to the view.
                return view_func(request, *args, **kwargs)
            elif request.user.is_itofficer:
                # User is authenticated but is an ocs, redirect to the home view.
                messages.error(
                    request,
                    "Only OCS are allowed to access this page. If you are an OCS, please log in with your account.",
                )
                return redirect(
                    "user_app:home"
                )  # Replace with the actual URL name of the home view.
            elif request.user.is_duty_officer:
                # User is authenticated but is a duty officer, redirect to the homepage view.
                messages.error(
                    request,
                    "Only OCS are allowed to access this page. If you are an OCS, please log in with your account.",
                )
                return redirect(
                    "user_app:home"
                )  # Replace with the actual URL name of the home view.
        else:
            # User is not authenticated, redirect to the login view.
            messages.error(
                request,
                "You need to log in as an OCS to access this page. If you do not have an account, please contact IT support for further assistance.",
            )
            return redirect(
                "login"
            )  # Replace with the actual URL name of the login view.

    return wrapper


def duty_officer_required(view_func):
    """
    decorator that ensures only duty officers can access a page
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_duty_officer:
                # User is authenticated and is a duty officer, allow access to the view.
                return view_func(request, *args, **kwargs)
            elif request.user.is_itofficer:
                # User is authenticated but is an ocs, redirect to the home view.
                messages.error(
                    request,
                    "Only duty officers are allowed to access this page. If you are a duty officer, please log in with your account.",
                )
                return redirect(
                    "user_app:home"
                )  # Replace with the actual URL name of the home view.
            elif request.user.is_ocs:
                # User is authenticated but is a duty officer, redirect to the homepage view.
                messages.error(
                    request,
                    "Only duty officers are allowed to access this page. If you are a duty officer, please log in with your account.",
                )
                return redirect(
                    "user_app:home"
                )  # Replace with the actual URL name of the home view.
        else:
            # User is not authenticated, redirect to the login view.
            messages.error(
                request,
                "You need to log in as a duty officers to access this page. If you do not have an account, please contact IT support for further assistance.",
            )
            return redirect(
                "login"
            )  # Replace with the actual URL name of the login view.

    return wrapper