from django.db import models
from django.contrib.auth.models import User

# # Create your models here.


class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creado = models.DateField(auto_now_add=True)
    fechaCom = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - creado por ' + self.user.username
