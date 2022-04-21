from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def itineraire(request):
    return HttpResponse("Liste des itinéraires")

@login_required
def sorties(request, itineraire_id):
    return HttpResponse("Liste des sorties de l'itinéraire %s" % itineraire_id)

@login_required
def sortie(request, sortie_id):
    return HttpResponse("Détail de la sortie %s" % sortie_id)

@login_required
def nouvelle_sortie(request):
    return HttpResponse("Page d'entrée de sortie")

@login_required
def modif_sortie(request, sortie_id):
    return HttpResponse("Page de modification de la sortie %s" % sortie_id)
