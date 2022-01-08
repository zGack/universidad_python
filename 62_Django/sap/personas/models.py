from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    num_calle = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"Domicilio {self.id}: {self.calle} {self.num_calle} {self.pais}"

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Persona {self.id}: {self.nombre} {self.apellido}"