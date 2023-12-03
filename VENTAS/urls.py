from django.urls import path
from VENTAS.views import carga_medicamento, carga_perfumeria, carga_suplemento

urlpatterns = [
    path("carga_medicamento", carga_medicamento, name = "carga medicamento"),
    path("carga_perfumeria", carga_perfumeria, name = "carga perfumeria"),
    path("carga_suplemento", carga_suplemento, name = "carga suplemento"),
]