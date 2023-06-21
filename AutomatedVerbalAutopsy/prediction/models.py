from django.db import models
from questionnaire.models import COD
# # Create your models here.
# questionaire_cod= COD.objects.get(id)



class Predictions(models.Model):
    cod = models.ForeignKey(COD, on_delete=models.CASCADE)
    # cod = models.OneToOneField(COD, on_delete=models.CASCADE, primary_key=True)
    sababu = models.CharField(max_length=50)

    def __str__(self):
        return self.cod.jina_kwanza
