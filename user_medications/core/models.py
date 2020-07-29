from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Medication(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
  nome = models.CharField(max_length=50)
  descricao = models.TextField(default="")
  validade = models.DateField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return '{} - {}'.format(self.nome, self.validade)
