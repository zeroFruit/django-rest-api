from django.urls import path

from user.views import CreateUserView, CreateTokenView


app_name = 'user'

urlpatterns = [
    path('', CreateUserView.as_view(), name='create'),
    path('token', CreateTokenView.as_view(), name='token')
]
