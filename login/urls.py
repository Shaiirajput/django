
from django.urls import path
from login.views import UserRegistrationView
from .import views



urlpatterns = [
    path('register/',views.UserRegistrationView.as_view(),name="register"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('profile/',views.UserProfileView.as_view(),name="profile"),
    path('changepassword/',views.UserChangePasswordView.as_view(),name="changepassword"),
    path('logout/',views.Logout.as_view(),name='logout'),


]
