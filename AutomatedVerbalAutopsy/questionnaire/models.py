from django.db import models
from django.utils import timezone




class Shuhuda(models.Model):
    Uhusiano_marehemu = (
        ('Baba', 'Baba'),
        ('Mama', 'Mama'),
        ('ndugu', 'ndugu'),
        ('Hakuna Uhusiano', 'Hakuna Uhusiano'),
        ('Nyingine','nyingine')
    )
    Uhusiano_kifo=(
        ('Ndio','Ndio'),
        ('Hapana','Hapana'),
    )
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    simu = models.CharField(max_length=100, default='')
    uhusiano = models.CharField(max_length=255, choices=Uhusiano_marehemu)
    uhusiano_kipindi_kifo = models.CharField(max_length=255, choices=Uhusiano_kifo)

    def __str__(self):
        return self.first_name


class Marehemu(models.Model):
    shuhuda=models.ManyToManyField(Shuhuda, verbose_name=("Shhuda_Wa_Kifo"))
    Ndoa = (
        ('ndoa', 'ndoa'),
        ('hajafunga ndoa', 'hajafunga ndoa'),
        ('mjane', 'mjane'),
        ('mgane', 'mgane'),
        ('talaka','talaka'),
        ('kutengana','kutengana')
    )
    Mahali = (
        ('nyumbani', 'nyumbani'),
        ('hospitali', 'hospitali'),
        ('kituo cha afya', 'kituo cha afya'),
        ('sijui', 'sijui')
    )
    Jinsia=(
        ('mume','mwanaume'),
        ('mke','mwanamke')
    )
    jina_kwanza = models.CharField(max_length=255 )
    jina_pili = models.CharField(max_length=255)
    jina_mwisho = models.CharField(max_length=255)
    jinsia = models.CharField(max_length=255, choices=Jinsia)
    ndoa = models.CharField(max_length=255, choices=Ndoa)
    kuzaliwa = models.DateField(default=timezone.now)
    kufa = models.DateField(default=timezone.now)
    mahali = models.CharField(max_length=255, choices=Mahali)
    maelezo = models.TextField()
 
    def __str__(self):
       return self.jina_kwanza


    
class Sababu(models.Model):
    Marehemu=models.OneToOneField(Marehemu, verbose_name=("Sababu_Ya_Kifo"), on_delete=models.CASCADE)
    sababu = models.CharField(max_length=255)

    def __str__(self):
       return self.sababu