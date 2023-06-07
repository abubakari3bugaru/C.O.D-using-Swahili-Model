from django.db import models
from  questionnaire.models import COD

# # Create your models here.
# questionaire_cod= COD.objects.get(id)
class Predictions(COD):
    sababu=models.CharField( max_length=50)


