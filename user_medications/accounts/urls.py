from user_medications.accounts.views import UserLoginAPIView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
  path('login', UserLoginAPIView.as_view())
]