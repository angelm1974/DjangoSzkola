from django.db import models

# Create your models here.

class Pytanie(models.Model):
    tekst_pytania=models.CharField(max_length=300)
    pub_date=models.DateTimeField('data publikacji')

class Odpowiedz(models.Model):
    pytanie=models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    tekst_wyboru=models.CharField(max_length=300)
    glosy=models.IntegerField(default=0)
        