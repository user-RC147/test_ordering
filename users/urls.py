from django.urls import path

from . import views


app_name='users'

urlpatterns = [
    path('',views.ViewUserPage.as_view(), name='user_page'),
    path('create/',views.CreateUserPage.as_view(), name='create_user'),
]
