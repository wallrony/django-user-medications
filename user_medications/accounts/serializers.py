from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  nome = serializers.CharField(source='get_full_name')

  class Meta:
    model = User
    fields = ('id', 'nome')

class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField(required=True)
  password = serializers.CharField(required=True)

  default_error_messages = {
    'inative_account': ('user account is disabled'),
    'invalid_credentials': ('unable to login with provided credentials')
  }

  def __init__(self, *args, **kwargs):
    super(UserLoginSerializer, self).__init__(*args, **kwargs)

  def validate(self, data):
    self.user = authenticate(username=data.get('username'), password=data.get('password'))

    if self.user:
      if not self.user.is_active:
        raise serializers.ValidationError(self.error_messages['inactive_account'])

      return data
    raise serializers.ValidationError(self.error_messages['invalid_credentials'])

class TokenSerializer(serializers.ModelSerializer):
  auth_token = serializers.CharField(source='key')
  user = UserSerializer(read_only=True)

  class Meta:
    model = Token
    fields = ('auth_token', 'user', 'created')