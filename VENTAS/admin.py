from django.contrib import admin

# Register your models here.
from VENTAS.models import medicamentos, perfumeria, suplementos

admin.site.register(medicamentos)
admin.site.register(perfumeria)
admin.site.register(suplementos)

