from django.urls import path
from .views import RegisterView ,ProfileView,ProfileUpdateView

urlpatterns = [
    path(
        "register/",
        RegisterView.as_view(),
        name="register",
    ),

   path(
    "me/",
    ProfileView.as_view(),
    name="profile",
   ),
   path(
       "profile/",
       ProfileUpdateView.as_view(),
       name="profile-update",
   )
]