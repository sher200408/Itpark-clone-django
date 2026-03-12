from django.urls import path
from .views import *

# 127.0.0.1:8000/
urlpatterns = [
    path('profile/<uuid:id>', profile, name="profile"),
    path('login/', login_user, name="login"),
    path('logout/', logouts, name="logout"),
    path('account/', account_user, name="account"),
    path('account_edit/', account_edit, name="account_edit"),
    path('register/', register_user_signup, name="register"),
    path('profiles_skill/', profiles_skill, name="profiles"),
    
]
