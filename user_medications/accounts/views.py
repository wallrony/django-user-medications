from rest_framework.authtoken.models import Token
from user_medications.accounts.serializers import UserLoginSerializer, TokenSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserLoginAPIView(GenericAPIView):
  serializer_class = UserLoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if serializer.is_valid():
      user = serializer.user
      token, _ = Token.objects.get_or_create(user=user)

      return Response(data=TokenSerializer(token).data)
    return Response({'message': 'authentication error'}, status=status.HTTP_400_BAD_REQUEST)