from django.urls import path
from .views import (
    register_user,
    login_user,
    homepage,
    logout_user,
    officer_list,
    delete_officer,
    update_officer,
)

app_name = "user_app"

urlpatterns = [
    path("", homepage, name="home"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("officer_list/", officer_list, name="officer_list"),
    path("delete_officer/<str:badge_number>/", delete_officer, name="delete_officer"),
    path('update_officer/<str:badge_number>/', update_officer, name='update_officer'),
   
]
