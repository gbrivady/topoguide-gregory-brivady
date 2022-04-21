from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Itineraire, Sortie

class IndexView(LoginRequiredMixin, generic.ListView):
    """
    View of all itineraires, for the home page
    """
    context_object_name = "all_itineraires"

    def get_queryset(self):
        # Return all the itineraires, ordered by title
        return Itineraire.objects.order_by("titre")

class DetailView(LoginRequiredMixin, generic.DetailView):
    """
    View all the informations of an Itineraire , and all the Sorties posted by users.
    """
    template_name = "itineraires/itineraire.html"
    model = Itineraire

class SortieView(LoginRequiredMixin, generic.DetailView):
    """
    View detailled information about a 'Sortie'
    """
    template_name = "itineraires/sortie.html"
    model = Sortie

@login_required
def nouvelle_sortie(request):
    return HttpResponse("Page d'entrée de sortie")

@login_required
def modif_sortie(request, sortie_id):
    return HttpResponse("Page de modification de la sortie %s" % sortie_id)