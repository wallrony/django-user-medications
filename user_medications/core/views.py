from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from user_medications.core.models import Medication
from user_medications.core.serializers import MedicationSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index_medications(request, user_id):
  if request.method != 'GET':
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

  try:
    medications = Medication.objects.filter(user_id=user_id)

    serializer = MedicationSerializer(medications, many=True)

    return Response(serializer.data)
  except Medication.DoesNotExist:
    return Response({'message': 'no content found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_medication(request):
  if request.method != 'POST':
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

  serializer = MedicationSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()

    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
  return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def in_unique_medication(request, medication_id):
  try:
    medication = Medication.objects.get(id=medication_id)
  except Medication.DoesNotExist:
    return Response({'message': 'no content found'}, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET':
    serializer = MedicationSerializer(medication)

    return Response(data=serializer.data)
  elif request.method == 'PUT':
    serializer = MedicationSerializer(medication, data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    medication.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
