from django.urls import path
from . import views


app_name = "itineraires"
urlpatterns = [
    path('', views.IndexView.as_view(), name="itineraire_list"),
    path('sorties/<int:pk>/', views.DetailView.as_view(), name = "itineraire"),

    path('sortie/<int:pk>', views.SortieView.as_view(), name="sortie"),
    
    path("nouvelle_sortie/", views.NewSortie.as_view(), name="nouvelle_sortie"),
    path("modif_sortie/<int:pk>/", views.EditSortie.as_view(), name="modif_sortie"),

]