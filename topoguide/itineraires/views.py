from django.http import HttpResponse

def itineraire(request):
    return HttpResponse("Liste des itinéraires")

def sorties(request, itineraire_id):
    return HttpResponse("Liste des sorties de l'itinéraire %s" % itineraire_id)

def sortie(request, sortie_id):
    return HttpResponse("Détail de la sortie %s" % sortie_id)

def nouvelle_sortie(request):
    return HttpResponse("Page d'entrée de sortie")

def modif_sortie(request, sortie_id):
    return HttpResponse("Page de modification de la sortie %s" % sortie_id)
