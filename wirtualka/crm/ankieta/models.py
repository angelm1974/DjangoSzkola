from django.db import models

# Create your models here.

class Pytanie(models.Model):
    tekst_pytania=models.CharField(max_length=300)
    pub_date=models.DateTimeField('data publikacji')
    
    def __str__(self):
        return self.tekst_pytania
    
    class Meta:
        verbose_name="Pytanie"
        verbose_name_plural="Pytania"

class Odpowiedz(models.Model):
    pytanie=models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    tekst_wyboru=models.CharField(max_length=300)
    glosy=models.IntegerField(default=0)
        
    def __str__(self):
        return self.tekst_wyboru
    
    class Meta:
        verbose_name="Odpowiedź"
        verbose_name_plural="Odpowiedzi"    