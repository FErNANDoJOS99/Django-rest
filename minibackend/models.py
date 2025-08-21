from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # se recomienda encriptarla

    def __str__(self):
        return self.nombre



# Se usa relacion uno a muchos
class Lista(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fechacreacion = models.CharField(max_length=128)  # se recomienda encriptarla
    usuario = models.ForeignKey(
        ##Esto apunta directamente a la PK de la tabla Usuario
        Usuario, 
        on_delete=models.CASCADE,  # Si se borra el usuario, se borran sus listas
        related_name="listas"   # permite acceder con usuario.listas.all()
    )

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=200)
    contenido=models.CharField(max_length=200)
    listas = models.ManyToManyField(Lista, related_name="articulos")

    def __str__(self):
        # Esto se ocupa cuando se hace print (es la variable que se imprime)
        return self.nombre