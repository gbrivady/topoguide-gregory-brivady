from pyexpat import model
from django.db import models
from django.conf import settings

class Itineraire(models.Model):
    """
    Contains the reference data for the experience shared by the users.
    """
    titre = models.CharField(max_length=200)
    start_point = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    start_altitude = models.IntegerField("Altitude au départ (m)")
    min_altitude = models.IntegerField("Altitude minimale (m)")
    max_altitude = models.IntegerField("Altitude maximale (m)")
    cumulated_slope_up = models.IntegerField("Dénivelé positif cumulé (m)")
    cumulated_slope_down = models.IntegerField("Dénivelé négatif cumulé (m)")
    estimated_duration = models.PositiveIntegerField("Temps estimé (h)")
    estimated_difficulty = models.PositiveSmallIntegerField(
        choices=[(i, "%s/5" %i) for i in range(1, 6)]
        )

class Sortie(models.Model):
    """
    The experiences shared by the users.
    """
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    itineraire = models.ForeignKey("Itineraire", on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.PositiveIntegerField("Durée réelle (h)")
    number_ppl = models.PositiveIntegerField("Nombre de participants (humains)")
    
    group_xp = models.CharField(
        "Expérience des participants à la sortie", max_length=20,
        choices=[(0, "Tous débutants"), (1, "Mixte"), (2, "Tous Expérimentés")], 
        )
    
    weather = models.CharField("Météo", max_length=8,
                               choices=[(0, "Bonne"), (1, "Moyenne"), (2, "Mauvaise")])

    difficulty = models.PositiveSmallIntegerField(
        "Difficulté ressentie", choices=[(i, "%s/5" %i) for i in range(1, 6)]
        )
