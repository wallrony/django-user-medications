from django.urls import path
from user_medications.core import views

app_name = 'core'

urlpatterns = [
  path('medications', views.add_medication),
  path('users/<int:user_id>/medications', views.index_medications),
  path('medications/<int:medication_id>', views.in_unique_medication)
]