from django.db import models

# Create your models here.
class Contact(models.Model):
    name_client=models.CharField(max_length=200,verbose_name="Nombre")
    lastname=models.CharField(max_length=200,verbose_name="Apellido")
    email=models.EmailField(max_length=254,verbose_name="Correo Electronico")
    date=models.DateField(null= True, blank=True,verbose_name='Fecha')
    guests=models.IntegerField(verbose_name="Huéspedes")
    message=models.TextField(verbose_name="mensaje")
    
    def __str__(self):
        return self.name_client