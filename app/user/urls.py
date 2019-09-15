from django.urls import path

from user.views import CreateUserView, CreateTokenView, ManageUserView


app_name = 'user'

urlpatterns = [
    path('', CreateUserView.as_view(), name='create'),
    path('token', CreateTokenView.as_view(), name='token'),
    path('me', ManageUserView.as_view(), name='me')
]
