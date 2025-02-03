from django.db import models
from django.contrib.auth.models import User

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='escudos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Jornada(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE, related_name='partidos')
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    goles_local = models.IntegerField(null=True, blank=True)
    goles_visitante = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"

class Prediccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predicciones')
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='predicciones')
    goles_local_pred = models.IntegerField()
    goles_visitante_pred = models.IntegerField()

    def calcular_puntos(self):
        partido = self.partido
        if partido.goles_local is not None and partido.goles_visitante is not None:
            if (self.goles_local_pred == partido.goles_local and
                self.goles_visitante_pred == partido.goles_visitante):
                return 3
            elif (self.goles_local_pred > self.goles_visitante_pred and
                partido.goles_local > partido.goles_visitante) or \
                (self.goles_local_pred < self.goles_visitante_pred and
                partido.goles_local < partido.goles_visitante) or \
                (self.goles_local_pred == self.goles_visitante_pred and
                partido.goles_local == partido.goles_visitante):
                return 1
        return 0

    def __str__(self):
        return f"{self.usuario.username} - {self.partido}"

class UsuarioQuiniela(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    puntos_totales = models.IntegerField(default=0)

    def __str__(self):
        return self.usuario.username