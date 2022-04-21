from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="itineraire_list"),
    path('sorties/<int:itineraire_id>/', views.sorties, name = "sorties_list"),
    
    path('sortie/<int:sortie_id>', views.sortie, name="sortie_details"),
    path("modif_sortie/<int:sortie_id>/", views.modif_sortie, name="modif_sortie"),
    path("nouvelle_sortie/", views.nouvelle_sortie, name="create_sortie"),
]
