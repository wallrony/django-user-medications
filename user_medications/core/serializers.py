from user_medications.core.models import Medication
from rest_framework import serializers

class MedicationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Medication
    fields = ('id', 'user_id', 'nome', 'descricao', 'validade', 'created_at')
