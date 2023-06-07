from django.urls import path, include
from . import views
# from django.urls import re_path

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
        name='authenticate_user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout')
]

