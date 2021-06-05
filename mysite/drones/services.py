import random
import threading
import math
from django.db import models
from .models import Drone, Zone, Simulation

# Distance Base <-> Zone en metres
distanceBaseZone = 1000
hauteur = 10
angle = 10


def calculLargeurZone(zone):
    return int(zone.long2) - int(zone.long)


def calculLongueurZone(zone):
    return int(zone.lat2) - int(zone.lat)


# Calcul du diamètre de la zone de blayage du capteur en fonction de la hauteur et de l'angle de balayage
def calculDiametreBalayage(hauteur, angle):
    # tan angle = rayon / hauteur
    return round(2 * math.tan(angle) * hauteur)


def calculNbBalayages(largeur, diametre):
    return round(largeur / diametre)


def calculDistanceZoneACouvrirParDrone(nbBalayages, largeur):
    return nbBalayages * largeur


def calculDistanceTotalParDrone(nbBalayages, largeur):
    return 2 * distanceBaseZone + calculDistanceZoneACouvrirParDrone(nbBalayages, largeur)


def calculTempsParcoursSection(drone, section):
    return section / (drone.vitesse * 100 / 6)


def calculConsoParcoursSection(drone, section):
    return drone.autonomie - calculTempsParcoursSection(drone, section)


def calculNbLongueurZoneParcourable(drone, longueur):
    # Autonomie restante du drone  = autonomie - A/R
    autonomieRestante = drone.autonomie - calculTempsParcoursSection(drone, 2 * distanceBaseZone)
    return round(autonomieRestante / calculTempsParcoursSection(drone, longueur))


def startSimulation(drone, zone):
    bilan = ""
    print("Démarrage de la simulation")
    print("- Autonomie drone : " + str(drone.autonomie))
    largeurZone = calculLargeurZone(zone)
    print("- Largeur zone : " + str(largeurZone))
    longueurZone = calculLongueurZone(zone)
    print("- Longueur zone : " + str(longueurZone))
    diam = calculDiametreBalayage(hauteur, angle)
    print("- Diametre du balayage: " + str(diam))
    nbParcoursZone = calculNbBalayages(largeurZone, diam)
    print("- Nombre d'A/R sur une zone pour la couvrir: " + str(nbParcoursZone))
    nbParcourableZone = calculNbLongueurZoneParcourable(drone, longueurZone)
    print("- Nombre d'A/R que le drone est en capacité de faire sur une zone: " + str(nbParcourableZone))

    # Est-ce que l'autonomie est suffisante pour parcourir une zone ?
    if (nbParcourableZone < nbParcoursZone):
        print("Le drone n'a pas l'autonomie suffisante pour parcourir toute la zone")
        bilan = "Le drone n'a pas l'autonomie suffisante pour parcourir toute la zone"
    else:
        print("Le drone peut parcourir toute la zone au moins une fois")
        print("Arrivée du drone sur zone ")
        autonomieRestante = drone.autonomie - calculTempsParcoursSection(drone, 2 * distanceBaseZone)
        print("Autonomie restante:" + str(autonomieRestante))
        # Démmarrage du feu sur un point aléatoire a parcourir
        distanceFeu = random.randrange(1, nbParcoursZone * longueurZone)
        # Découverte du feu
        nbPacouruZone = round(distanceFeu / longueurZone)
        tpsEcouleDecouvertefeu = calculTempsParcoursSection(drone, distanceBaseZone + distanceFeu)
        bilan = "Le feu a été découvert en : " + str(round(tpsEcouleDecouvertefeu)) + " minutes"
        print(bilan)
    return bilan
