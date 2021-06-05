from django.db import models


class Drone(models.Model):
    # id = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    marque = models.CharField(max_length=20)
    modele = models.CharField(max_length=20)
    poids = models.IntegerField(default=0)
    autonomie = models.IntegerField(default=0)
    vitesse = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Zone(models.Model):
    # id = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    long = models.CharField(max_length=20)
    lat2 = models.CharField(max_length=20)
    long2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Simulation(models.Model):
    name = models.CharField(max_length=20)
    Drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    Zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    bilan = models.CharField(default="Aucun bilan disponible",max_length=200)

    def __str__(self):
        return self.name
