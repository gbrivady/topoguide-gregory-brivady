from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
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

class NewSortie(LoginRequiredMixin, generic.edit.CreateView):
    template_name = "itineraires/sortie_edit.html"
    model = Sortie
    fields = ['date', 'duration', 'number_ppl', 'group_xp', 'weather', 'difficulty']
    
    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.itineraire = Itineraire.objects.get(id=self.request.GET.get("i"))
        return super().form_valid(form)

class EditSortie(LoginRequiredMixin, generic.edit.UpdateView):
    template_name = "itineraires/sortie_edit.html"
    model = Sortie
    fields = ['date', 'duration', 'number_ppl', 'group_xp', 'weather', 'difficulty']
    def form_valid(self, form):
        if(self.request.user == form.instance.writer):
            return super().form_valid(form)
        else:
            return HttpResponseForbidden("Vous n'avez pas le droit de modifier une sortie dont vous n'êtes pas l'auteur.")